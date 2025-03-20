from Persona import Persona

class Docente(Persona):
    def __init__(self, identificacion, nombre, apellido, edad, facultad):
        super().__init__(identificacion, nombre, apellido, edad)
        self.facultad = facultad
    
    def __str__(self):
        return f"{super().__str__()}, Facultad: {self.facultad}"

class GestorDocentes:
    def __init__(self):
        self.docentes = {}
    
    def agregar(self, identificacion, nombre, apellido, edad, facultad):
        if identificacion in self.docentes:
            return False
        self.docentes[identificacion] = Docente(identificacion, nombre, apellido, edad, facultad)
        return True
    
    def consultar(self, identificacion=None):
        if identificacion is None:
            return list(self.docentes.values())
        return self.docentes.get(identificacion)
    
    def actualizar(self, identificacion, nombre=None, apellido=None, edad=None, facultad=None):
        if identificacion not in self.docentes:
            return False
        docente = self.docentes[identificacion]
        if nombre:
            docente.nombre = nombre
        if apellido:
            docente.apellido = apellido
        if edad:
            docente.edad = edad
        if facultad:
            docente.facultad = facultad
        return True
    
    def eliminar(self, identificacion):
        if identificacion not in self.docentes:
            return False
        del self.docentes[identificacion]
        return True