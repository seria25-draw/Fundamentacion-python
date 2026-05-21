precios = [2500, 1800, 3000, 5000]

for precio in precios:
    if precio < 2000:
        print("Barato: ", precio)
    elif precio <= 4000:
        print("Moderado: ", precio)
    else:
        print("Caro: ", precio)