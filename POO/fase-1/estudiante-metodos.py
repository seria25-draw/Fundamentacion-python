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
    

e1 = Estudiante("juanita", 3.9)

print(e1.mostrar_info())