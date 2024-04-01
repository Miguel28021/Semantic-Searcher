from fileHandler import fileHandler
from embeddingModel import EmbeddingModel

fileH = fileHandler()
corpus = fileH.load_file("articles.ris")

embedder = EmbeddingModel("FremyCompany/BioLORD-2023",corpus)

while(1):
    # Leer la entrada del teclado y almacenarla en una variable
    entrada = input("Por favor, introduce una consulta: ")

    if entrada == "fin":
        break

    result=embedder.launch_query(entrada)

embedder.delete_DB()
