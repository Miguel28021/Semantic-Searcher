import streamlit as st
import pandas as pd
import numpy as np

#from streamlit import session_state

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

# Mostrar un spinner mientras se carga la página
with st.spinner('Cargando modelo'):

    load_model()
    #st.success('¡Modelo cargado correctamente!')

model = load_model()

st.title("Buscador Semántico")
with st.sidebar:
    st.write("Filtros:")
query = st.text_input("query", placeholder="Haz una pregunta de carácter científico", label_visibility="hidden")

if query:
    results=model.launch_query(query,50)

    data = {
        "Id": [objeto.id for objeto in results],
        "Titulo": [objeto.title for objeto in results],
        "Año": [objeto.year for objeto in results],
        "Autores": [objeto.authors for objeto in results],
        "URL": [objeto.url for objeto in results],
        "Abstract": [objeto.abstract for objeto in results]
    }
    pd.set_option('display.max_colwidth', None)

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(data)
    # styler = df.style
    # styler.set_table_styles([
    #     {"selector": "tr", "props": "line-height: 500px;"}

    # ])
    st.dataframe(df,height=600,hide_index=True)#,use_container_width=True)

