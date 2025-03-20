from Persona import Persona

class Administrativo(Persona):
    def __init__(self, identificacion, nombre, apellido, edad, area, cargo):
        super().__init__(identificacion, nombre, apellido, edad)
        self.area = area
        self.cargo = cargo
    
    def __str__(self):
        return f"{super().__str__()}, Área: {self.area}, Cargo: {self.cargo}"

class GestorAdministrativos:
    def __init__(self):
        self.administrativos = {}
    
    def agregar(self, identificacion, nombre, apellido, edad, area, cargo):
        if identificacion in self.administrativos:
            return False
        self.administrativos[identificacion] = Administrativo(identificacion, nombre, apellido, edad, area, cargo)
        return True
    
    def consultar(self, identificacion=None):
        if identificacion is None:
            return list(self.administrativos.values())
        return self.administrativos.get(identificacion)
    
    def actualizar(self, identificacion, nombre=None, apellido=None, edad=None, area=None, cargo=None):
        if identificacion not in self.administrativos:
            return False
        administrativo = self.administrativos[identificacion]
        if nombre:
            administrativo.nombre = nombre
        if apellido:
            administrativo.apellido = apellido
        if edad:
            administrativo.edad = edad
        if area:
            administrativo.area = area
        if cargo:
            administrativo.cargo = cargo
        return True
    
    def eliminar(self, identificacion):
        if identificacion not in self.administrativos:
            return False
        del self.administrativos[identificacion]
        return True