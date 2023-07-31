from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    INP = "joao"
    return render_template("index.html", Uname=INP)

@app.route("/treinamento", methods=["POST"])
def treinamento():
    treino = request.form["treino"]
    return f"<h2>Treino enviado: {treino}</h2>"

if __name__ == "__main__":
    app.run()
