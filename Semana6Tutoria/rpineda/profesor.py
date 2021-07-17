class Profesor:
    def __init__(self,nombre,dni,edad,correo):
        self.nombres = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
    
    def __str__(self) -> str:
        return f"{self.nombres} {self.dni} {self.edad} {self.correo}"
