class Curso():
    def __init__(self,id,nombre):
        self.nombre = nombre
        self.id = id
        
    def __str__(self) -> str:
        return f"{self.nombre} {self.id}"