from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
api = "https://api.hgbrasil.com/weather"
# A API usada é fornecida pelo site HGBrasil.com

key = "87d7c4fb" # key da API HG Brasil

def getData(city):
    dados = requests.get(api, params={"city_name": city, "key":key})
    dadosp = dados.json()
    return dadosp

@app.route("/") # Rota principal
def index():
    return render_template("index.html", titulo="Home")

@app.route("/rio")
def rio():
    data = getData("Rio de Janeiro, RJ")
    return render_template("dados.html", titulo="Clima RJ", dados=data)

@app.route("/sp")
def sp():
    data = getData("São Paulo, SP")
    return render_template("dados.html", titulo="Clima SP", dados=data)

@app.route("/mangaratiba")
def mangaratiba():
    data = getData("Mangaratiba, RJ")
    return render_template("dados.html", titulo="Clima Mangaratiba, RJ", dados=data)

@app.route("/salvador")
def salvador():
    data = getData("Salvador, BA")
    return render_template("dados.html", titulo="Clima Salvador, BA", dados=data)

@app.route("/portoalegre")
def portoalegre():
    data = getData("Porto Alegre, RS")
    return render_template("dados.html", titulo="Clima Porto Alegre, RS", dados=data)

app.run()