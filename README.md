
# Semantic-Searcher

This project consists of a search engine specialized in carrying out semantic searches in scientific texts which contain biomedical concepts and clinical sentences, in order to retrieve the most relevant articles to answer a query. To achieve this, I have implemented a Streamlit application which uses sentence similarity models to calculate the vector embeddings and ChromaDB to store this embeddings. All of the articles that the application uses are referenced in the `articles.ris` file. Alternatively, you can  upload your own RIS file. The main objective of the project is to offer an alternative to traditional search engines, wich only look for keyword matches and do not take into account the overall meaning of the query.

![semantic-searcher-high-resolution-logo](https://github.com/Miguel28021/Semantic-Searcher/assets/128999129/bfbbf6bb-3643-49ae-8b0c-966d287f9f08)


# Installation 

To use the application, you need to have python installed on your computer, as well as all of the dependencies listed on the `requirements.txt` file. For the latter, you can use the following command:

`pip install -r requirements.txt`

#Falta probar si hace falta algo más

# Usage

Once all of the dependencies required by the project have been installed, you can execute it by positioning yourself in the `application` folder and typing the following command:

`streamlit run .\app_streamlit.py`

This will launch the Semantic Searcher website in localhost:8501.

First you need to select your own ris file or use the default file: "Articles.ris", which contains over 2000 articles from the drug repurposing field.


Now you need to select which one of the three models available the system is going to use to generate the embeddings. After this the sytem loads the model and generates the embeddings of the documents. Keep in mind that this process takes its time (especially if you choose BioLORD-2023 and S-BioELECTRA, due to the higher dimensions of the embeddings).


Now you can write a query and the application will show the 100 most relevant documents. Additionally, you can filter these documents by type of article, year, title and author.

![Captura de pantalla 2024-06-03 202713](https://github.com/Miguel28021/Semantic-Searcher/assets/128999129/6ea5ad6b-edcf-43f6-96f8-40e085f8ce2c)
# License

The Semantic-Searcher application is licensed under the GNU General Public License v3.0.

# Contact

If you have any questions or suggestions regarding the proyect you can reach me at malomaosorio@gmail.com
