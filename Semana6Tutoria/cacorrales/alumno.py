class Alumno():
    def __init__(self,nombre,dni,edad,correo):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.dni} {self.edad} {self.correo}"