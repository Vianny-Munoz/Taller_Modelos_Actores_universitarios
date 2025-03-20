from Administrativo import GestorAdministrativos
from Docente import GestorDocentes
from Estudiante import GestorEstudiantes

class MenuPrincipal:
    def __init__(self):
        self.gestor_estudiantes = GestorEstudiantes()
        self.gestor_docentes = GestorDocentes()
        self.gestor_administrativos = GestorAdministrativos()
    
    def mostrar_menu_principal(self):
        print("\n===== SISTEMA DE GESTIÓN =====")
        print("1. Gestionar Estudiantes")
        print("2. Gestionar Docentes")
        print("3. Gestionar Administrativos")
        print("0. Salir")
        return input("Seleccione una opción: ")
    
    def mostrar_submenu(self, tipo):
        print(f"\n===== GESTIÓN DE {tipo.upper()} =====")
        print(f"1. Crear {tipo}")
        print(f"2. Ver {tipo}s")
        print(f"3. Ver detalles de un {tipo}")
        print(f"4. Actualizar {tipo}")
        print(f"5. Eliminar {tipo}")
        print("0. Volver al menú principal")
        return input("Seleccione una opción: ")
    
    def crear_estudiante(self):
        try:
            print("\n----- Crear Estudiante -----")
            codigo = input("COD: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            
            if self.gestor_estudiantes.agregar(codigo, nombre, apellido, edad, carrera, semestre):
                print("Estudiante creado con éxito!")
            else:
                print("Error: Ya existe un estudiante con ese código.")
        except:
            print("Ocurrio un Error en el ingreso de datos")
    
    def ver_estudiantes(self):
        print("\n----- Lista de Estudiantes -----")
        estudiantes = self.gestor_estudiantes.consultar()
        if not estudiantes:
            print("No hay estudiantes registrados.")
            return
        for estudiante in estudiantes:
            print(estudiante)
    
    def ver_detalle_estudiante(self):
        codigo = input("Ingrese el código del estudiante: ")
        estudiante = self.gestor_estudiantes.consultar(codigo)
        if estudiante:
            print("\n----- Detalles del Estudiante -----")
            print(estudiante)
        else:
            print("Estudiante no encontrado.")
    
    def actualizar_estudiante(self):
        codigo = input("Ingrese el código del estudiante a actualizar: ")
        estudiante = self.gestor_estudiantes.consultar(codigo)
        if not estudiante:
            print("Estudiante no encontrado.")
            return
        
        print("\n----- Actualizar Estudiante -----")
        print("Deje en blanco si no desea modificar el campo")
        
        nombre = input(f"Nombre [{estudiante.nombre}]: ")
        apellido = input(f"Apellido [{estudiante.apellido}]: ")
        edad_str = input(f"Edad [{estudiante.edad}]: ")
        edad = int(edad_str) if edad_str else None
        carrera = input(f"Carrera [{estudiante.carrera}]: ")
        semestre_str = input(f"Semestre [{estudiante.semestre}]: ")
        semestre = int(semestre_str) if semestre_str else None
        
        if self.gestor_estudiantes.actualizar(codigo, nombre, apellido, edad, carrera, semestre):
            print("Estudiante actualizado con éxito!")
        else:
            print("Error al actualizar el estudiante.")
    
    def eliminar_estudiante(self):
        codigo = input("Ingrese el código del estudiante a eliminar: ")
        if self.gestor_estudiantes.eliminar(codigo):
            print("Estudiante eliminado con éxito!")
        else:
            print("Error: Estudiante no encontrado.")
    
    def crear_docente(self):
        try:
            print("\n----- Crear Docente -----")
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            departamento = input("Departamento: ")
            
            if self.gestor_docentes.agregar(identificacion, nombre, apellido, edad, departamento):
                print("Docente creado con éxito!")
            else:
                print("Error: Ya existe un docente con esa Identificación.")
        except:
            print("Ocurrio un Error en el ingreso de datos")
    
    def ver_docentes(self):
        print("\n----- Lista de Docentes -----")
        docentes = self.gestor_docentes.consultar()
        if not docentes:
            print("No hay docentes registrados.")
            return
        for docente in docentes:
            print(docente)
    
    def ver_detalle_docente(self):
        identificacion = input("Ingrese la identificación del docente: ")
        docente = self.gestor_docentes.consultar(identificacion)
        if docente:
            print("\n----- Detalles del Docente -----")
            print(docente)
        else:
            print("Docente no encontrado.")
    
    def actualizar_docente(self):
        identificacion = input("Ingrese la identificación del docente a actualizar: ")
        docente = self.gestor_docentes.consultar(identificacion)
        if not docente:
            print("Docente no encontrado.")
            return
        
        print("\n----- Actualizar Docente -----")
        print("Deje en blanco si no desea modificar el campo")
        
        nombre = input(f"Nombre [{docente.nombre}]: ")
        apellido = input(f"Apellido [{docente.apellido}]: ")
        edad_str = input(f"Edad [{docente.edad}]: ")
        edad = int(edad_str) if edad_str else None
        departamento = input(f"Departamento [{docente.departamento}]: ")
        
        if self.gestor_docentes.actualizar(identificacion, nombre, apellido, edad, departamento):
            print("Docente actualizado con éxito!")
        else:
            print("Error al actualizar el docente.")
    
    def eliminar_docente(self):
        identificacion = input("Ingrese la identificación del docente a eliminar: ")
        if self.gestor_docentes.eliminar(identificacion):
            print("Docente eliminado con éxito!")
        else:
            print("Error: Docente no encontrado.")
    
    def crear_administrativo(self):
        try:
            print("\n----- Crear Administrativo -----")
            identificacion = input("identificación: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            area = input("Área: ")
            cargo = input("Cargo: ")
            
            if self.gestor_administrativos.agregar(identificacion, nombre, apellido, edad, area, cargo):
                print("Administrativo creado con éxito!")
            else:
                print("Error: Ya existe un administrativo con esa identificación.")
        except:
            print("Ocurrio un Error en el ingreso de datos")
    
    def ver_administrativos(self):
        print("\n----- Lista de Administrativos -----")
        administrativos = self.gestor_administrativos.consultar()
        if not administrativos:
            print("No hay administrativos registrados.")
            return
        for administrativo in administrativos:
            print(administrativo)
    
    def ver_detalle_administrativo(self):
        identificacion = input("Ingrese la identificación del administrativo: ")
        administrativo = self.gestor_administrativos.consultar(identificacion)
        if administrativo:
            print("\n----- Detalles del Administrativo -----")
            print(administrativo)
        else:
            print("Administrativo no encontrado.")
    
    def actualizar_administrativo(self):
        identificacion = input("Ingrese la identificación del administrativo a actualizar: ")
        administrativo = self.gestor_administrativos.consultar(identificacion)
        if not administrativo:
            print("Administrativo no encontrado.")
            return
        
        print("\n----- Actualizar Administrativo -----")
        print("Deje en blanco si no desea modificar el campo")
        
        nombre = input(f"Nombre [{administrativo.nombre}]: ")
        apellido = input(f"Apellido [{administrativo.apellido}]: ")
        edad_str = input(f"Edad [{administrativo.edad}]: ")
        edad = int(edad_str) if edad_str else None
        area = input(f"Área [{administrativo.area}]: ")
        cargo = input(f"Cargo [{administrativo.cargo}]: ")
        
        if self.gestor_administrativos.actualizar(identificacion, nombre, apellido, edad, area, cargo):
            print("Administrativo actualizado con éxito!")
        else:
            print("Error al actualizar el administrativo.")
    
    def eliminar_administrativo(self):
        identificacion = input("Ingrese la identificación del administrativo a eliminar: ")
        if self.gestor_administrativos.eliminar(identificacion):
            print("Administrativo eliminado con éxito!")
        else:
            print("Error: Administrativo no encontrado.")
    
    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == "0":
                print("Hasta pronto!")
                break
            
            elif opcion == "1":
                while True:
                    subopcion = self.mostrar_submenu("Estudiante")
                    if subopcion == "0":
                        break
                    elif subopcion == "1":
                        self.crear_estudiante()
                    elif subopcion == "2":
                        self.ver_estudiantes()
                    elif subopcion == "3":
                        self.ver_detalle_estudiante()
                    elif subopcion == "4":
                        self.actualizar_estudiante()
                    elif subopcion == "5":
                        self.eliminar_estudiante()
                    else:
                        print("Opción no válida")
            
            elif opcion == "2":
                while True:
                    subopcion = self.mostrar_submenu("Docente")
                    if subopcion == "0":
                        break
                    elif subopcion == "1":
                        self.crear_docente()
                    elif subopcion == "2":
                        self.ver_docentes()
                    elif subopcion == "3":
                        self.ver_detalle_docente()
                    elif subopcion == "4":
                        self.actualizar_docente()
                    elif subopcion == "5":
                        self.eliminar_docente()
                    else:
                        print("Opción no válida")
            
            elif opcion == "3":
                while True:
                    subopcion = self.mostrar_submenu("Administrativo")
                    if subopcion == "0":
                        break
                    elif subopcion == "1":
                        self.crear_administrativo()
                    elif subopcion == "2":
                        self.ver_administrativos()
                    elif subopcion == "3":
                        self.ver_detalle_administrativo()
                    elif subopcion == "4":
                        self.actualizar_administrativo()
                    elif subopcion == "5":
                        self.eliminar_administrativo()
                    else:
                        print("Opción no válida")
            
            else:
                print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ejecutar()