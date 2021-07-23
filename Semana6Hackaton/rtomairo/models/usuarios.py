class Persona:
    def __init__(self,nombre, dni, edad, correo):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
    def __str__(self):
        return f"{self.nombre} {self.dni} {self.edad} {self.correo} "


class Alumno(Persona):
    def __init__(self,codigo, nombre, dni, edad, correo):
        super().__init__(nombre, dni, edad, correo)
        self.codigo = codigo
    def __str__(self):
        return super().__str__()+f"{self.codigo}"

class Profesor(Persona):
    def __init__(self,codigo, nombre, dni, edad, correo):
        super().__init__(nombre, dni, edad, correo)
        self.codigo = codigo
    def __str__(self):
        return super().__str__() + f"{self.codigo}"