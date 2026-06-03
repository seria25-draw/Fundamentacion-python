class Usuario:
    def __init__(self,documento,nombre,correo,estado,rol):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo 
        self.estado = estado
        self.rol    = rol

    def mostrar_info(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Correo: {self.correo}, Estado: {self.estado}, Rol: {self.rol}"

class SistemaUsuarios:
    def __init__(self):
        self.usuarios=[]

    def registrar_usuario(self):

        documento = input("Ingrese el documento del usuario sin puntos: ")

        if documento == "":
            print("El documento no puede estar vacío")
            return

        for us in self.usuarios:
            if us.documento == documento:
                print("Error: El documento ya existe")
                return

        nombre = input("Ingrese el nombre del usuario: ")

        if nombre == "":
            print("El nombre no puede estar vacío")
            return

        while True:

            correo = input("Ingrese el correo del usuario: ")

            if correo == "":
                print("El correo no puede estar vacío")
                continue

            if "@" not in correo or "." not in correo:
                print("Error: El correo no es válido")
                continue

            estado = input("Ingrese el estado del usuario (Activo/Inactivo): ")

            if estado == "":
                print("El estado no puede estar vacío")
                continue

            if estado.lower() not in ["activo", "inactivo"]:
                print("Estado no válido")
                continue

            print("""
            ===== ROLES =====
            1. Administrador
            2. Aprendiz
            3. Instructor
            =================
            """)

            opcion_rol = input("Seleccione el rol: ")

            if opcion_rol == "1":
                rol = "Administrador"
            elif opcion_rol == "2":
                rol = "Aprendiz"
            elif opcion_rol == "3":
                rol = "Instructor"
            else:
                print("Rol no válido")
                continue

            nuevo_usuario = Usuario(
            documento,
            nombre,
            correo,
            estado,
            rol
            )

            self.usuarios.append(nuevo_usuario)

            print("Usuario registrado correctamente")
            break

    def mostrar_usuarios(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            print("\nLISTA DE USUARIOS")
            for us in self.usuarios:
                print(us.mostrar_info())
        
    def buscar_usuario(self):
        print("""
        ===== BUSCAR USUARIO =====
        1. Buscar por documento
        2. Buscar por correo
        =========================
        """)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            documento = input("Ingrese el documento: ")

            for us in self.usuarios:
                if us.documento == documento:
                    print("\nUsuario encontrado:")
                    print(us.mostrar_info())
                    return

            print("Usuario no encontrado")

        elif opcion == "2":
            correo = input("Ingrese el correo: ")

            for us in self.usuarios:
                if us.correo == correo:
                    print("\nUsuario encontrado:")
                    print(us.mostrar_info())
                    return

            print("Usuario no encontrado")

        else:
            print("Opcion invalida")

    def eliminar_usuario(self):
        documento = input("Ingrese el documento del usuario a eliminar: ")
        for us in self.usuarios:
            if us.documento == documento:
                self.usuarios.remove(us)
                print("Usuario eliminado correctamente")
                return

        print("Usuario no encontrado")
        
    def guardar_archivo(self):
        with open("usuarios.txt", "w") as archivo:
            for us in self.usuarios:
                archivo.write(us.mostrar_info() + "\n")

            print("Archivo guardado correctamente")
        
    def menu(self):
        while True:

            print("""
                ============= MENU =============
                1. Registrar usuario
                2. Mostrar usuarios
                3. Buscar usuario
                4. Actualizar usuario
                5. Eliminar usuario
                6. Mostrar usuarios activos
                7. Contar usuarios por rol
                8. Guardar archivo
                9. Salir
                ================================
                """)

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.mostrar_usuarios()
            elif opcion == "3":
                self.buscar_usuario()
            elif opcion == "4":
                self.actualizar_usuario()
            elif opcion == "5":
                self.eliminar_usuario()
            elif opcion == "6":
                self.mostrar_activos()
            elif opcion == "7":
                self.contar_roles()
            elif opcion == "8":
                self.guardar_archivo()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opcion invalida")

sistema = SistemaUsuarios()
sistema.menu()
