import streamlit as st
from PIL import Image

def phase1():
    image = Image.open('img/main.bmp')
    st.image(image, use_column_width='auto')
    st.markdown("""
                <br/><div style="text-align: center; font-size: 30px">
                    Proyecto realizado gracias al dataset <b>Million Song Dataset</b><br/>
                    y a los datos extraidos de <b>MusicBrainz</b> y <b>Echo Nest</b>
                </div>
            """, unsafe_allow_html=True)