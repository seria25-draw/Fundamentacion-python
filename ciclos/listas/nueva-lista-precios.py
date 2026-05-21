precios = [2500, 1800, 3000, 5000]

precios_con_iva = []

for precio in precios:
    impuesto = precio + (precio * 0.19) #2500 + (2500 * 0.19) = 2975
    precios_con_iva.append(impuesto)
print("Precios con IVA: ", precios_con_iva)
