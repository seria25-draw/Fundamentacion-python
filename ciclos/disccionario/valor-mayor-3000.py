productos = {
    "Arroz:": 2500,
    "Leche:": 1800,
    "Pan:": 3000,
    "Frutas:": 5000
}

for nombre, precio in productos.items():
    if precio > 3000:
        print(nombre , "es caro COP", precio)