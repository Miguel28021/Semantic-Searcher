from sentence_transformers import SentenceTransformer
sentences = ["Cat scratch injury", "Cat scratch disease", "Bartonellosis"]

model = SentenceTransformer('FremyCompany/BioLORD-2023')
embeddings = model.encode(sentences)
print(embeddings)