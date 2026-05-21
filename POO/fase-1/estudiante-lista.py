class Estudiante:
    #agregar atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

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
    nota = float(input("Nota: "))

    e = Estudiante(nombre, nota)
    estudent.append(e)

print("\nLista de estudiante")
for est in estudent:
    print(est.mostrar_info())