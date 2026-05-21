productos = {
    "Arroz:": 2500,
    "Leche:": 1800,
    "Pan:": 3000,
    "Frutas:": 5000
}
# como no se va a calcular se usa items() para obtener el nombre y el precio de cada producto
for nombre, precio in productos.items():
    print(nombre,precio)
   