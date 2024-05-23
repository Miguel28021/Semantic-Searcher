import rispy
import sys
import os.path
import re

m_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/models/')
print(m_dir)
sys.path.append(m_dir)
from dataModels import Corpus,Doc # type: ignore

class fileHandler:

    def __init__(self):
        pass

    def load_file(self,file):
        
        if isinstance(file, str):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            articles_file = os.path.join(script_dir, 'articles.ris')
            records = rispy.load(open(articles_file, 'r',encoding="utf8"))
        else:
            contenido_ris=file.getvalue().decode("utf-8") 
            records = rispy.loads(contenido_ris)
        
        corpus: Corpus = []
        id = 0
        i=0
        for record in records:
            if "abstract" in record.keys():
                if("authors" in record.keys()):
                    authors = ''.join(record["authors"][0:])
                else:
                    authors = "unknown"

                if("urls" in record.keys()):
                    urls = record["urls"][0]
                else:
                    urls = "unknown" 
                

                corpus.append(Doc(id=id,title=record["title"][0:],type=record["type_of_reference"][0:],year=record["publication_year"][0:],url=urls,authors=authors,abstract=record["abstract"][0:]))              

                id+=1
                if id == 100:
                    break

        return corpus