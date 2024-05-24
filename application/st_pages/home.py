import streamlit as st
import pandas as pd

import sys
import os

fh_dir = (os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'),'..'))
+ '/fileHandling/')
em_dir = (os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'),'..'))+ '/embeddings/')
sys.path.append(fh_dir)
sys.path.append(em_dir)

from fileHandler import fileHandler # type: ignore
from embeddingModel import EmbeddingModel # type: ignore


@st.cache_resource(show_spinner=False)
def load_model(file,model):
    fileH = fileHandler()
    corpus = fileH.load_file(file)
    return EmbeddingModel(model,corpus)
    
def show_data(results,col2):
    data = {
        "Score": [objeto.score for objeto in results],
        "Type": [objeto.type for objeto in results],
        "Title": [objeto.title for objeto in results],
        "Year": [objeto.year for objeto in results],
        "Authors": [objeto.authors for objeto in results],
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
        st.session_state['apply_filter'] = False
        st.session_state['filter'] = ""
        st.session_state['filter_type'] = ""

        
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        
        var1 = st.empty()
        var2 = st.empty()
        var3 = st.empty()
        var4 = st.empty()

        if st.session_state['loaded'] == False:

            if var1.button("Use articles.ris"):
                st.session_state['uploaded'] = True

            st.session_state["uploaded_file"] =var2.file_uploader("Or upload your own RIS file",type=".ris")

            if  st.session_state["uploaded_file"] :
                st.session_state['uploaded'] = True               
            
            if st.session_state['uploaded'] == True:
                var1.empty()
                var2.empty()

                with col2:
                    selected_model = var3.selectbox("Model selection:",("BioS-MiniLM","BioLORD-2023","S-BioELECTRA"))
                    if selected_model == "BioS-MiniLM":
                        st.session_state["model"] = "menadsa/BioS-MiniLM"
                    elif selected_model == "BioLORD-2023":     
                        st.session_state["model"] = "FremyCompany/BioLORD-2023"
                    elif selected_model == "S-BioELECTRA":
                        st.session_state["model"] = "menadsa/S-BioELECTRA"

                if var4.button("Load"):
                    st.session_state['loaded']=True

        if st.session_state['loaded'] == True:

            var3.empty()
            var4.empty()

            with st.spinner('Loading ' + str(st.session_state["model"].split('/')[1]) + " model"):
               if st.session_state["uploaded_file"]:            
                    model=load_model(st.session_state["uploaded_file"],st.session_state["model"])
               else:
                    model=load_model("articles.ris",st.session_state["model"])

            with col2:
                query = st.text_input("query", placeholder="Formulate a scientific query", label_visibility="hidden")

            with col3:
                st.write("")
                with st.expander("Filter by:"):
                    filter_type = st.selectbox(
                    "What filter do you want to apply?",
                    ("","Tiype of article", "Year", "Title","Author"),label_visibility="hidden")

                    if filter_type == "Tiype of article":
                        filter = st.selectbox(
                        "What type of article are you looking for?",
                        ("Journal","Book", "Book chapter", "Conference proceedings"))
                    elif filter_type == "Year":                            
                        fecha_inicio=st.text_input("From")
                        fecha_final=st.text_input("To")

                    elif filter_type == "Title":
                        filter = st.text_input("What is the title of the article?")
                    elif filter_type == "Author":
                        filter = st.text_input("Who is the author of the article?")
                    else:
                        filter = ""
                        st.session_state['apply_filter'] = False
                        
                    if st.button("Apply"):
                        # Paramater check
                        if filter_type == "Year":
                            if not fecha_inicio.isdigit() or not fecha_final.isdigit():
                                st.write("Dates must be positive integers")
                            else:
                                if int(fecha_inicio) > int(fecha_final):
                                    st.write("Final date must be greater than initial date")
                                else:
                                    if query:
                                        st.session_state['apply_filter'] = True
                                        st.session_state['filter'] = fecha_inicio + "-" + fecha_final
                                        st.session_state['filter_type'] = filter_type
                                    else:
                                        st.write("You must introduce a query before applying a filter")
                        elif filter:
                            if query:
                                st.session_state['apply_filter'] = True
                                st.session_state['filter'] = filter
                                st.session_state['filter_type'] = filter_type
                            else:
                                st.write("You must introduce a query before applying a filter")
                    
            if query:

                if  st.session_state['apply_filter'] == False:
                    results=model.launch_query(query,"","",50)
                else:
                    results=model.launch_query(query,st.session_state['filter_type'],st.session_state['filter'],50)
                    
                show_data(results,col2)



                        

                
                
                    
