import streamlit as st
from PIL import Image
from phases import phase1
from phases import phase2
from phases import phase3
from phases import phase4
from phases import phase5
from phases import phase6
from phases import phase7


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
    '5. Haciendo recomendaciones',
    '6. Planificación a futuro',
    '7. Agradecimientos'
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
elif selectedPhase == '6. Planificación a futuro':
    phase6.phase6()
elif selectedPhase == '7. Agradecimientos':
    phase7.phase7()

st.sidebar.markdown("""
    ***
    **Daniel Vivas - Febrero 2022**
    contacto@danielvivas.com
""")