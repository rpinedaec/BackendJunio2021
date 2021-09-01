class Salon:
    def __init__(self,codigo_salon,nombre,anio_escolar,id_curso=0):
        self.codigo_salon = codigo_salon,
        self.nombre = nombre,
        self.anio_escolar = anio_escolar,
        self.id_curso = id_curso


    def __str__(self):
        return f"{self.codigo_salon} - {self.nombre} - {self.anio_escolar} - {self.id_curso}"