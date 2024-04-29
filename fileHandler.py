import rispy
from dataModels import Corpus,Doc

class fileHandler:

    def __init__(self):
        pass

    def load_file(self,file):
        
        print(file)
        if isinstance(file, str):
            print("La variable es una cadena de texto")
            records = rispy.load(open(file, 'r',encoding="utf8"))
        else:
            print("La variable no es una cadena de texto")
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
                
                corpus.append(Doc(id=id,title=record["title"][0:],tipo=record["type_of_reference"][0:],year=record["publication_year"][0:],url=urls,authors=authors,abstract=record["abstract"][0:]))              

                id+=1
                i+=1
                # if i == 50:
                #     break

        return corpus