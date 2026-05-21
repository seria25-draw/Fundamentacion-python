class Estudiante:
    #agregar atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

#crear los objetos
e1 = Estudiante("juan",4.2)
print("Nombre", e1.nombre)

e2 = Estudiante ("maria", 2.5)
print("Nombre", e2.nombre)