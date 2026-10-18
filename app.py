from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/criacao-de-sites")
def criacao_de_sites():
    return render_template("criacao_sites.html")

@app.route("/criacao-de-bots")
def criacao_de_bots():
    return render_template("criacao_bots.html")

@app.route("/fileflow")
def fileflow():
    return render_template("fileflow.html")

if __name__ == "__main__":
    app.run(debug=True)
