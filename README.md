
# Semantic Searcher

This project consists of a search engine specialized in carrying out semantic searches in scientific texts which contain biomedical concepts and clinical sentences. To achieve this, I have implemented a Streamlit application which uses sentence similarity models to do the vector embeddings and ChromaDB to store this vectors. The main objective of the project is to offer an alternative to traditional search engines, wich only look for keyword matches and do not take into account the overall meaning of the query.

# Installation 

To use the application, you need to have python installed on your computer, as well as all of the dependencies listed on the `requirements.txt` file. For the latter, you can use the following command:

`pip install -r requirements.txt`

# Usage

Once all of the dependencies required by the project have been installed, you can execute it by positioning yourself in the `application` folder and typing the following command:

`streamlit run .\app_streamlit.py`

This will launch the Semantic Searcher website in localhost:8501

# License

# Contact
