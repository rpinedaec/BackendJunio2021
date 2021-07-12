class Curso:
    def __init__(self,codigo_curso,nombre,activo,id_profesor=0):
        self.codigo_curso = codigo_curso,
        self.nombre = nombre,
        self.activo = activo,
        self.id_profesor = id_profesor
        

    def __str__(self):
        return f"{self.codigo_curso} - {self.nombre} - {self.activo}"

        