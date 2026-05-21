precios = [2500, 1800, 3000, 5000]

suma = 0

for precio in precios:
    suma += precio
    promedio = suma / len(precios)

print("Promedio de precios: ", promedio)