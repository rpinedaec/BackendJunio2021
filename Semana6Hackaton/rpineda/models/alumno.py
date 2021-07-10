import persona

class Alumno(Persona):
    def __init__(self,codigo, nombre, dni, edad, correo):
        super().__init__(nombre, dni, edad, correo)
        self.codigo = codigo