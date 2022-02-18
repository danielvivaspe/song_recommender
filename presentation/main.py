import streamlit as st
from PIL import Image
from phases import phase1
from phases import phase2
from phases import phase3
from phases import phase4
from phases import phase5

import os

st.set_page_config(page_title='SONG RECOMMENDER', page_icon='img/msd.png', layout='wide')

image = Image.open('img/msd.png')
st.sidebar.image(image)

st.sidebar.markdown("""
                ## <br/><div style="text-align: center">RECOMENDADOR DE CANCIONES</div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("""***""")

selectedPhase = st.sidebar.selectbox('Fase', [
    '1. Introducción',
    '2. Fuentes',
    '3. Limpieza y preparación de los datos',
    '4. Entendiendo el recomendador',
    '5. Haciendo recomendaciones'
])

if selectedPhase == '1. Introducción':
    phase1.phase1()
elif selectedPhase == '2. Fuentes':
    phase2.phase2()
elif selectedPhase == '3. Limpieza y preparación de los datos':
    phase3.phase3()
elif selectedPhase == '4. Entendiendo el recomendador':
    phase4.phase4()
elif selectedPhase == '5. Haciendo recomendaciones':
    phase5.phase5()

st.sidebar.markdown("""
    ***
    **Daniel Vivas - Febrero 2022**
    contacto@danielvivas.com
""")