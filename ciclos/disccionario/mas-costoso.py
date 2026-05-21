productos = {
    "Arroz:": 2500,
    "Leche:": 1800,
    "Pan:": 3000,
    "Frutas:": 5000
}


# mayor = 0

# producto_mayor= ""

# for  nombre, precio in productos.items():
#     if precio > mayor:
#         mayor = precio
#         producto_mayor = nombre

# print("Producto mas costoso:", nombre, "-", mayor)

precios = list(productos.values())
mayor = precios[0]
producto_mayor = ""

for nombre, precio in productos.items():
    if precio > mayor:
        mayor = precio
        producto_mayor = nombre

print("Producto mas costoso:", producto_mayor, "-", mayor)