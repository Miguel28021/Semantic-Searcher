import streamlit as st
import pandas as pd
from fileHandler import fileHandler
from embeddingModel import EmbeddingModel

@st.cache_resource(show_spinner=False)
def load_model(file="articles.ris"):
    print("CARGANDO LIBRERIAS")

    fileH = fileHandler()
    corpus = fileH.load_file(file)
    #model = EmbeddingModel("FremyCompany/BioLORD-2023",corpus)
    model = EmbeddingModel("menadsa/BioS-MiniLM",corpus)
    return model

def show_home():
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        #Mostrar un spinner mientras se carga la página
        with st.spinner('Cargando modelo'):
            var1 = st.empty()
            uploaded_file = var1.file_uploader("Sube un archivo .ris",type=".ris")
            if uploaded_file:
                var1.empty()
                contenido_ris=uploaded_file.getvalue().decode("utf-8")
                model=load_model(contenido_ris)
                with col3:
                    st.write("")
                    with st.expander("Filtrar por:"):
                        filter_type = st.selectbox(
                        "Que filtro quieres aplicar?",
                        ("","Tipo de publicación", "Año", "Titulo","Autor"),label_visibility="hidden")

                        if filter_type == "Tipo de publicación":
                            publication_type = st.selectbox(
                            "¿Que tipo de publicación buscas?",
                            ("Artículo de Revista","Libro", "Sección de Libro", "Actas de Conferencia"))
                        elif filter_type == "Año":
                            st.text_input("Desde")
                            st.text_input("Hasta")
                        elif filter_type == "Titulo":
                            st.text_input("¿Cual es el titulo de la publicación?")
                        elif filter_type == "Autor":
                            st.text_input("¿Cual es el autor de la publicación?")

                with col2:

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

                    df = pd.DataFrame(data)

                    with col2:
                        st.dataframe(df,height=600,hide_index=True)          

                
                
                    
