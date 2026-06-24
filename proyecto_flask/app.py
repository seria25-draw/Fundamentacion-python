from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return("Bienvenido a mi aplicacion flask ")

@app.route("/productos")
def productos():
    return "Listas de productos"

app.run(debug=True)