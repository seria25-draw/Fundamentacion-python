class Estudiante:
    contadorAprobados = 0
    contadorNoAprobados=0
    #agregar atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        if self.nota >=3:
            Estudiante.contadorAprobados += 1
        else:
            Estudiante.contadorNoAprobados += 1

    def mostrar_info(self):
        if self.nota >=3:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Estado: {estado}"
    
estudent =[]

for i in range(3):
    print(f"\nRegistro del estudiante {i+1}")
    nombre =input("Nombre: ")

    while True:
        nota = float(input("Ingrese la nota (0-5): "))
        if nota >= 0 and nota<= 5:
            break
        else:
            print("nota no valida")

    e = Estudiante(nombre, nota)
    estudent.append(e)

print("\nLista de estudiante")
for est in estudent:
    print(est.mostrar_info())

print("\n ---Resumen---")
print("la cantida de aprobados son: ", Estudiante.contadorAprobados)
print("la cantida de aprobados son: ", Estudiante.contadorNoAprobados)