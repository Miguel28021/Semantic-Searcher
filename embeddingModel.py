from sentence_transformers import SentenceTransformer, util
from dataModels import Corpus, Result
#from utils import print_resuts
 
class EmbeddingModel:
    def __init__(self, model_name, corpus:Corpus):
        self.model = SentenceTransformer(model_name)
        self.corpus = corpus
        self.document_embeddings = self.model.encode([doc["content"] for doc in self.corpus])
    
    def launch_query(self, query, k=5):
        query_embedding = self.model.encode(query)
        cos_sim_scores = util.cos_sim(query_embedding, self.document_embeddings).tolist()[0]
        results = [ Result(id=i, content=doc["content"], category= doc["category"], score=cos_sim_scores[i] )
                   for i, doc in enumerate(self.corpus) ]
        
        sorted_results = sorted(results, key=lambda x: x.score, reverse=True)
 
        print(sorted_results[:k])
 
        return sorted_results
    

