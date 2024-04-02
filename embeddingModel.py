from sentence_transformers import SentenceTransformer, util
import chromadb
from chromadb.utils import embedding_functions
from dataModels import Corpus, Result
#from utils import print_resuts
 
class EmbeddingModel:
    def __init__(self, model_name, corpus:Corpus):
        self.model = SentenceTransformer(model_name)
        self.corpus = corpus
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

        self.client = chromadb.Client()
        self.semanticDB = self.client.create_collection(name="SemanticDB",embedding_function = sentence_transformer_ef)
        self.semanticDB.add(
            documents=[doc["content"] for doc in self.corpus],
            metadatas=[doc for doc in self.corpus],
            ids=[str(doc["id"]) for doc in self.corpus]
        )    
    
    def launch_query(self, query, k=5):
        results = self.semanticDB.query(
            query_texts = query,
            n_results=k,
        )
        
        docs = results['metadatas'][0]
        scores = results['distances'][0]

        results = [ Result(id=doc['id'], content=doc['content'], category=doc['category'], score=scores[i] )
        for i, doc in enumerate(docs) ]

        print(results[0])
        return results
    
    def delete_DB(self):
        self.client.delete_collection("SemanticDB")
    

