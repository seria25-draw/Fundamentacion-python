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
    
nombre = input("Ingrese el nombre: ")
nota = float(input("Ingrese su nota: "))

e1 = Estudiante(nombre, nota)

print(e1.mostrar_info())