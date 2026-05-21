class Persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad
       

e1 = Persona("miguel",18)
print(f"Nombre: {e1.nombre}, Edad: {e1.edad}")

e2 = Persona("fernando",35)
print(f"Nombre: {e2.nombre}, Edad: {e2.edad}")
