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

@app.route('/procesar', methods=['POST'])
def procesar():
    query = request.form['texto']
    result=embedder.launch_query(query)
    return render_template("resultado.html", texto=result)

if __name__ == "__main__":
    app.run(debug=True)