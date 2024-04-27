import rispy
from dataModels import Corpus,Doc

class fileHandler:

    def __init__(self):
        pass

    def load_file(self,file_path):

        records = rispy.load(open(file_path, 'r',encoding="utf8"))
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
                if i == 200:
                    break

        return corpus