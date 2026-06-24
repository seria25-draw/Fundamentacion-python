from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return("Bienvenido al sistema")

@app.route("/saludo")
def saludo():
    return("Hola aprendiz ADSO")

@app.route("/inventario")
def inventario():
    return("Sistema inventario activo")

@app.route("/usuarios")
def usuarios():
    return("Sistema usuario activo")

# @app.route("/usuario/<nombre>")
# def usuario(nombre):
#     return f"Bienvenido: {nombre}"

app.run(debug=True)