from fileHandler import fileHandler
from embeddingModel import EmbeddingModel

fileH = fileHandler()
corpus = fileH.load_file("articles.ris")

embedder = EmbeddingModel("FremyCompany/BioLORD-2023",corpus)
embedder.launch_query("How much protein")