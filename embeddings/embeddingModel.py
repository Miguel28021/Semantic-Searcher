from sentence_transformers import SentenceTransformer, util
import chromadb
from chromadb.utils import embedding_functions
from dataModels import Corpus, Result  # type: ignore
 
class EmbeddingModel:
    def __init__(self, model_name, corpus:Corpus):
        self.model = SentenceTransformer(model_name)
        self.corpus = corpus
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        self.client = chromadb.Client()

        self.semanticDB = self.client.get_or_create_collection(name="SemanticDB",embedding_function = sentence_transformer_ef)

        self.semanticDB.add(
            documents=[doc["abstract"] for doc in self.corpus],
            metadatas=[doc for doc in self.corpus],
            ids=[str(doc["id"]) for doc in self.corpus]
        )    
    
    def launch_query(self, query,filter_type,filter,k):
        query_results = self.semanticDB.query(
            query_texts = query,
            n_results=k,
        )
        
        sorted_docs = query_results['metadatas'][0]
        distances = query_results['distances'][0]
        results=[]

        for i,doc in enumerate(sorted_docs):
            if filter_type == "" :
                results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
            
            elif filter_type == "Type of article":

                if filter == "Journal" and doc['type'] == "JOUR": 
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
                elif filter == "Book" and doc['type'] == "BOOK": 
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
                elif filter == "Book chapter" and doc['type'] == "CHAP": 
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
                elif filter == "Conference proceedings" and doc['type'] == "CONF": 
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
            
            elif filter_type == "Year":
                fecha_inicio, fecha_final = map(int, filter.split('-'))
                if int(doc["year"]) >= fecha_inicio and int(doc["year"]) <= fecha_final:
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))
                
            elif filter_type == "Title":
                if filter.lower() in doc['title'].lower():
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))

            elif filter_type == "Author":
                if filter.lower() in doc['authors'].lower():
                    results.append(Result(id=doc['id'],type=doc['type'],title=doc['title'],year=doc['year'],url=doc['url'],authors=doc['authors'], abstract=doc['abstract'], distance=distances[i]))

        return results
    
    

