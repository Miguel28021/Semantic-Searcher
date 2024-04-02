from flask import Flask, render_template,url_for,request
from fileHandler import fileHandler
from embeddingModel import EmbeddingModel

app = Flask(__name__)

fileH = fileHandler()
corpus = fileH.load_file("articles.ris")

embedder = EmbeddingModel("FremyCompany/BioLORD-2023",corpus)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=['POST'])
def enviar():
    query = request.form["texto"]
    results=embedder.launch_query(query)
    return render_template("resultado.html", texto='<br><br>'.join(str(objeto) for objeto in results))

if __name__ == "__main__":
    app.run(debug=True)