# contar productos menores q 2000

productos = {
    "Arroz:": 2500,
    "Leche:": 1800,
    "Pan:": 3000,
    "Frutas:": 5000
}

contador = 0

for precio in productos.values():
    if precio < 2000:
        contador += 1

print("Productos baratos: ",contador)