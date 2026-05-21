precios = [2500, 1800, 3000, 5000]

mayor = precios[0]

for precio in precios:
    if precio > mayor:
        mayor = precio

print("Precio más alto: ", mayor)