class Salon():
    def __init__(self,id,nombre,periodo_id,profesor_id,alumno_id):
          self.id = id
          self.nombre = nombre
          self.periodo_id = periodo_id
          self.profesor_id = profesor_id
          self.alumno_id = alumno_id

    def __str__(self) -> str:
        return f"{self.id} {self.nombre} {self.periodo_id} {self.profesor_id} {self.alumno_id}"