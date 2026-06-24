from flask import Flask

app = Flask(__name__)

@app.route("/contacto")
def contacto():
    return("Pagina de contacto ")

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"Bienvenido: {nombre}"

app.run(debug=True)