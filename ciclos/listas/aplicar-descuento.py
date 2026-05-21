precios = [2500, 1800, 3000, 5000]

for precio in precios:
    descuento = precio * 0.10
    nuevo_precio = precio - descuento

print("Nuevo precio: ", nuevo_precio)