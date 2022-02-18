import streamlit as st
import pickle
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'src\\')))
#os.chdir('../')
from recommender.DVrecommender import DVrecommender
from spotify.DVspotify import DVspotify

real_path = os.path.realpath('../')
spotify_lib = DVspotify()
#recom_lib = DVrecommender(n_rows=50000, max_play_scaling=5, triplets_path= real_path+'\\src\\data\\raw\\TasteProfile\\train_triplets.txt')
recom_lib = DVrecommender(triplets_path= real_path+'\\src\\data\\raw\\TasteProfile\\train_triplets.txt', n_rows=100000)
recom_lib.init_model(test=True)

def removeOutliers(dtf, *columns):
    for i in range(len(columns)):
        q_low = dtf[columns[i]].quantile(0.01)
        q_hi = dtf[columns[i]].quantile(0.99)
        dtf = dtf[(dtf[columns[i]] < q_hi) & (dtf[columns[i]] > q_low)]
    return dtf

def prediction(user, song):
    return recom_lib.get_estimation(user, song)

def prediction_10(user):
    preds = recom_lib.get_top_recommendations(user, 50)
    print(preds)
    recs = []
    for i in range(len(preds)):
        song = get_full_song(preds.iloc[i]['songID'], True)
        if song != "ID not found":
            recs.append({'song': get_full_song(preds.iloc[i]['songID'], True), 'est': preds.iloc[i]['est'], 'sptfID': spotify_lib.msd_id_to_spotify_id(preds.iloc[i]['songID'])})
    return recs


def get_full_song(songID, translate):
    print('MSD ID:' + songID)
    print('Full name', spotify_lib.get_full_name(songID, True))
    return spotify_lib.get_full_name(songID, translate)


def phase5():
    st.markdown(len(recom_lib.unique_users()))
    st.markdown(len(recom_lib.unique_songs()))

    st.markdown("""
                # Fase 5: Haciendo recomendaciones
                #### Vamos a empezar a hacer recomendaciones con el modelo generado
                ***
                ##### Probamos primero con uno de los usuarios del dataframe:
                """)
    st.text('')

    #df = pd.read_csv('../src/data/raw/TasteProfile/train_triplets.txt', sep='\t',
                           #names=['user', 'item', 'rating'], nrows=50000)

    selectedUser = st.selectbox('Usuario:', recom_lib.unique_users()[:500])

    st.markdown("""<br/><div style="text-align: justify; font-size: 12px; margin-top: -50px;">Extraidos 20 
                usuarios a modo representativo. Los usuarios están completamente anonimizados por 
                motivos de privacidad por lo que no se pueden extraer datos de los mismos.</div>
                """, unsafe_allow_html=True)

    listened = recom_lib.triplets_df[recom_lib.triplets_df['user'] == selectedUser]['item'].unique()

    with st.expander('El usuario ha escuchado ' + str(len(listened)) + ' canciones. Mostramos las primeras 10:'):

        if selectedUser != "":
            for song in listened[:10]:
                st.markdown('- ' + get_full_song(song, True))


    st.markdown('##### Calculamos el top de canciones que le vamos a recomendar')
    with st.expander('¿Qué nos recomienda nuestro modelo?'):

        preds = prediction_10(selectedUser)

        for i in range(len(preds)):
            if preds[i]['est'] != 1:
                text = 'veces'
            else:
                text = 'vez'
            st.markdown('['+preds[i]['song']+'](https://open.spotify.com/track/'+preds[i]['sptfID']+' "Escuchar '+preds[i]['song']+'")' + ' (' + str(preds[i]['est']) + ' '+text+')')





    #https://towardsdatascience.com/building-a-music-recommendation-engine-with-probabilistic-matrix-factorization-in-pytorch-7d2934067d4a
    #https://www.aprendemachinelearning.com/sistemas-de-recomendacion/















    st.markdown('Más información: https://thingsolver.com/introduction-to-recommender-systems/')
