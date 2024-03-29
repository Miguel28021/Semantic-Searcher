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
                corpus.append(Doc(id=id,category=record["publication_year"][0:],content=record["abstract"][0:]))
                id+=1
                i+=1
                if i == 100:
                    break

        return corpus