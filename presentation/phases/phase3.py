import streamlit as st

import pandas as pd

def phase3():
    st.markdown("""
            # Fase 3: Limpieza y preparación de los datos
            #### Una vez descargados todos los datos, hay que prepararlos para su análisis.
            ***
            ##### Partimos de los siguientes dataframes:
            """)
    st.text('')

    st.markdown('#### Metadata')
    df1 = pd.read_csv('../src/data/raw/MillionSongSubset/SongCSV.csv', nrows=500)
    st.dataframe(df1)
    st.markdown('Para generar este dataframe se ha necesitado extraer previamente toda la información contenida'
                'en el subset de MSD, ya que se descargan en ficheros con formato .h5')

    with st.expander('Transformación del dataset'):
        st.markdown("""
            - Retiramos las columnas con gran cantidad de nulos: **ArtistLatitude**, **ArtistLongitude** y **SongHotttnesss**
            - Retiramos las columnas **Energy** y **Danceability** por tener todo ceros, y **Year** por tener la mayoría
            - Retiramos la columna **Confidence**, **ArtistLocation**, **KeySignature** y **EndOfFadeIn** por tener gran cantidad de valores vacíos
            - Borramos los registros de **Tempo**, **TimeSignature**, **Title** and **ArtistHotttnesss** que tengan NaNs
            - Tratamos los strings para quitar las comillas y la b
        """)

    st.markdown('#### Triplets')
    df2 = pd.read_csv('../src/data/raw/TasteProfile/train_triplets_sample.txt', nrows=500, index_col=0)
    st.dataframe(df2)


    st.text('')
    st.text('')
    st.markdown("""
                ##### Transformación de los datos:
                """)



    with st.expander('Triplets'):
        st.markdown("""
            - El dataset es muy sencillo, por lo que no requiere modificaciones
            - Creamos una versión más liviana del fichero para poder alojarlo en github
        """)

    st.text('')



    st.markdown('### Juntamos ambos datasets')

    df3 = pd.read_csv('../src/data/processed/fulldata_sample.csv', nrows=500, index_col=0)
    st.dataframe(df3)

