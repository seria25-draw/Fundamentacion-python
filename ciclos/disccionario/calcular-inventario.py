productos = {
    "Arroz:": 2500,
    "Leche:": 1800,
    "Pan:": 3000,
    "Frutas:": 5000
}


total = 0
for precio in productos.values():
    total += precio
print("Total del inventario: ", total)