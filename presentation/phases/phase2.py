import streamlit as st

def phase2():

    st.markdown("""
        # Fase 2: Elección de fuentes
        #### El proyecto gira en torno a The Million Song Dataset, un dataset único en internet con un tamaño de casi 300 GB.
        ###### Para este proyecto se ha utilizado un 1% de dicho dataset.
        ***
        """)
    st.text('')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('img/msd.png', use_column_width='auto')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">Publicado en 2012, pretende incentivar a la investigación en el terreno musical. Contiene millones de registros únicos con varios metadatos de cada canción.</div>
            """, unsafe_allow_html=True)

    with col2:
        st.image('img/echonest.jpg', use_column_width='auto')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">Proporciona el "Taste Profile", una tripleta de datos anonimizados de la reproduccion de canciones por los usuarios.</div>
            """, unsafe_allow_html=True)

    with col3:
        st.image('img/spotify.png', use_column_width='auto')
        st.markdown("""
            ##### <br/><div style="text-align: justify; padding: 0 7px 0 7px;">También se ha usado la API de Spotify para recopilar datos de reproducciones propias y generar recomendaciones en una futura versión del proyecto.</div>
            """, unsafe_allow_html=True)

    st.text('')
    st.text('')
    st.text('')
    st.image('img/labrosa.png', use_column_width='auto')
    st.markdown("""
        #### <br/><div style="text-align: center">The Million Song Dataset es un proyecto de labROSA</div>
    """, unsafe_allow_html=True)
    st.markdown("""
            <br/><div style="text-align: center; font-size: 13px; color:gray;">The Echo Nest Taste profile subset, the official user data collection for the<br/>
            Million Song Dataset, available at: http://millionsongdataset.com/tasteprofile</div>
        """, unsafe_allow_html=True)
    st.markdown("""
                <br/><div style="text-align: center; font-size: 13px; color:gray;">Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere.<br/>
                    The Million Song Dataset. In Proceedings of the 12th International Society<br/>
                    for Music Information Retrieval Conference (ISMIR 2011), 2011.</div>
            """, unsafe_allow_html=True)