from persona import Persona

class Profesor(Persona):
    def __init__(self,id,nombre,dni,edad,correo):
          super().__init__(nombre, dni, edad, correo)
          self.id = id

    def __str__(self) -> str:
        return f"{self.id} {self.nombre} {self.dni} {self.edad} {self.correo}"