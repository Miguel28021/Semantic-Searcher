import os
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_navigation_bar import st_navbar

def wide_space_default():
    st.set_page_config(layout="wide")


@st.cache_resource(show_spinner=False)
def load_model():
    print("CARGANDO LIBRERIAS")
    from fileHandler import fileHandler
    from embeddingModel import EmbeddingModel
    fileH = fileHandler()
    corpus = fileH.load_file("articles.ris")
    #model = EmbeddingModel("FremyCompany/BioLORD-2023",corpus)
    model = EmbeddingModel("menadsa/BioS-MiniLM",corpus)
    return model

wide_space_default()
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    }, "img": {
        "padding-right": "14px",
        "justify-content": "left",
        
    },
    "div": {
        "max-width": "32rem",
    },
    
    "span": {
        "color": "white",
        "padding": "44px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "44px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
page = st_navbar(["Subir archivo","Acerca de", "Contacto"],logo_path=logo_path,styles=styles)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    # Mostrar un spinner mientras se carga la página
    with st.spinner('                  Cargando modelo y liberías'):
        load_model()


with col3:
    st.write("")
    with st.expander("Filtrar por:"):
        option = st.selectbox(
        'Que filtro quieres aplicar?',
        ('Tipo de publicación', 'Año', 'Fechar',"Autor"),label_visibility="hidden")

        st.write('You selected:', option)

model = load_model()

with col2:
    #st.write("prueba")
    #st.title("Buscador Semántico")

    query = st.text_input("query", placeholder="Haz una pregunta de carácter científico", label_visibility="hidden")

if query:
    results=model.launch_query(query,50)

    data = {
        "Tipo": [objeto.tipo for objeto in results],
        "Titulo": [objeto.title for objeto in results],
        "Año": [objeto.year for objeto in results],
        "Autores": [objeto.authors for objeto in results],
        "URL": [objeto.url for objeto in results],
        "Abstract": [objeto.abstract for objeto in results]
    }
    pd.set_option('display.max_colwidth', None)

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(data)

    with col2:
        st.dataframe(df,height=600,hide_index=True)#,use_container_width=True)
    
