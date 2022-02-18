import streamlit as st

import pandas as pd
import plotly.express as px

def phase4():
    st.markdown("""
                # Fase 4: Entendiendo el recomendador
                #### ¿Como funciona un recomendador?
                """)


    st.markdown('## Tipos de recomendadores:')
    st.image('img/rec_types.png')
    st.markdown('### Algunos ejemplos son:')
    st.markdown('- Top 10 canciones más escuchadas')
    st.markdown('- Otros usuarios como tú han escuchado')
    st.markdown('- Los usuarios que han escuchado las mismas canciones que tú también han escuchado')
    st.markdown('Nos vamos a basar en el filtro colaborativo basado en usuarios')

    st.markdown('---')

    st.markdown('## ¿Y como funciona la recomendación?')
    st.markdown('##### Se que mis usuarios han escuchado canciones. También se cuántas veces han escuchado mis usuarios cada cancion:')
    st.image('img/matrix.png')
    st.markdown('En este ejemplo los usuarios están valorando frutas. Aplicado al recomendador, la fruta son las canciones y las valoraciones son la cantidad de veces que han escuchado la canción.')

    st.markdown('##### Estas matrices tienden a ser de tipo sparse (dispersas). El algoritmo elegido debe evitar ser afectado por la dispersión.')



    #https://towardsdatascience.com/building-a-music-recommendation-engine-with-probabilistic-matrix-factorization-in-pytorch-7d2934067d4a
    #https://www.aprendemachinelearning.com/sistemas-de-recomendacion/















    st.markdown('Más información: https://thingsolver.com/introduction-to-recommender-systems/')




