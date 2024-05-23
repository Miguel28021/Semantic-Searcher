import streamlit as st
import pandas as pd

import sys
import os

fh_dir = (os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'),'..'))
+ '/fileHandling/')
em_dir = (os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'),'..'))+ '/embeddings/')
sys.path.append(fh_dir)
sys.path.append(em_dir)

from fileHandler import fileHandler
from embeddingModel import EmbeddingModel


@st.cache_resource(show_spinner=False)
def load_model(file,model):
    fileH = fileHandler()
    corpus = fileH.load_file(file)
    return EmbeddingModel(model,corpus)
    
def show_data(results,col2):
    data = {
        "Score": [objeto.score for objeto in results],
        "Tipo": [objeto.type for objeto in results],
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

def show_home():
    st.empty()

    if 'uploaded' not in st.session_state:
        st.session_state['loaded'] = False
        st.session_state["model"] = ""
        st.session_state['uploaded'] = False
        st.session_state["file"] = ""
        st.session_state['aplicar_filtro'] = False
        st.session_state['filter'] = ""
        st.session_state['filter_type'] = ""

        
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        
        var1 = st.empty()
        var2 = st.empty()
        var3 = st.empty()
        var4 = st.empty()

        if st.session_state['loaded'] == False:

            if var1.button("Utilizar fichero articles.ris"):
                st.session_state['uploaded'] = True

            st.session_state["uploaded_file"] =var2.file_uploader("O sube tu propio archivo .ris",type=".ris")

            if  st.session_state["uploaded_file"] :
                st.session_state['uploaded'] = True               
            
            if st.session_state['uploaded'] == True:
                var1.empty()
                var2.empty()

                with col2:
                    selected_model = var3.selectbox("Seleccion de modelo:",("BioS-MiniLM","BioLORD-2023","S-BioELECTRA"))
                    if selected_model == "BioS-MiniLM":
                        st.session_state["model"] = "menadsa/BioS-MiniLM"
                    elif selected_model == "BioLORD-2023":     
                        st.session_state["model"] = "FremyCompany/BioLORD-2023"
                    elif selected_model == "S-BioELECTRA":
                        st.session_state["model"] = "menadsa/S-BioELECTRA"

                if var4.button("Cargar"):
                    st.session_state['loaded']=True

        if st.session_state['loaded'] == True:

            var3.empty()
            var4.empty()

            with st.spinner('Cargando modelo ' + st.session_state["model"]):
               if st.session_state["uploaded_file"]:            
                    model=load_model(st.session_state["uploaded_file"],st.session_state["model"])
               else:
                    model=load_model("articles.ris",st.session_state["model"])

            with col2:
                query = st.text_input("query", placeholder="Formula una pregunta de investigación", label_visibility="hidden")

            with col3:
                st.write("")
                with st.expander("Filtrar por:"):
                    filter_type = st.selectbox(
                    "Que filtro quieres aplicar?",
                    ("","Tipo de publicación", "Año", "Titulo","Autor"),label_visibility="hidden")

                    if filter_type == "Tipo de publicación":
                        filter = st.selectbox(
                        "¿Que tipo de publicación buscas?",
                        ("Artículo de Revista","Libro", "Sección de Libro", "Actas de Conferencia"))
                    elif filter_type == "Año":                            
                        fecha_inicio=st.text_input("Desde")
                        fecha_final=st.text_input("Hasta")

                    elif filter_type == "Titulo":
                        filter = st.text_input("¿Cual es el titulo de la publicación?")
                    elif filter_type == "Autor":
                        filter = st.text_input("¿Cual es el autor de la publicación?")
                    else:
                        filter = ""
                        st.session_state['aplicar_filtro'] = False
                        
                    if st.button("Aplicar"):
                        #Comprobación de parametros
                        if filter_type == "Año":
                            if not fecha_inicio.isdigit() or not fecha_final.isdigit():
                                st.write("Las fechas deben ser numeros positivos")
                            else:
                                if int(fecha_inicio) > int(fecha_final):
                                    st.write("La fecha inicial no puede ser mayor que la final")
                                else:
                                    if query:
                                        st.session_state['aplicar_filtro'] = True
                                        st.session_state['filter'] = fecha_inicio + "-" + fecha_final
                                        st.session_state['filter_type'] = filter_type
                                    else:
                                        st.write("Debes introducir una pregunta antes de aplicar el filtro")
                        elif filter:
                            if query:
                                st.session_state['aplicar_filtro'] = True
                                st.session_state['filter'] = filter
                                st.session_state['filter_type'] = filter_type
                            else:
                                st.write("Debes introducir una pregunta antes de aplicar el filtro")
                    
            if query:

                if  st.session_state['aplicar_filtro'] == False:
                  #  st.write("No se aplica ningun filtro")
                    results=model.launch_query(query,"","",50)
                else:
                   # st.write("Se aplica el filtro de " + st.session_state['filter_type'] + " = " + st.session_state['filter'])
                    results=model.launch_query(query,st.session_state['filter_type'],st.session_state['filter'],50)
                    
                show_data(results,col2)



                        

                
                
                    
