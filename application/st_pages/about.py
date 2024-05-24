import streamlit as st


def show_about():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("""This project consists of a search engine specialized in carrying out semantic searches in scientific texts 
                 which contain biomedical concepts and clinical sentences. To achieve this, I have implemented a Streamlit application 
                 which uses sentence similarity models to do the vector embeddings and ChromaDB to store this vectors. The main objective 
                 of the project is to offer an alternative to traditional search engines, wich only look for keyword matches and do not 
                 take into account the overall meaning of the query.""")