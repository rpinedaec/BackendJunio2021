class Alumno():
    def __init__(self,
                 codigo_alumno,
                 nombres,
                 apellido_paterno,
                 apellido_materno,
                 edad,
                 correo,
                 direccion,
                 id_salon = 0):
        self.codigo_alumno = codigo_alumno
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.correo = correo
        self.direccion = direccion
        self.id_salon = id_salon
    
    def __str__(self) -> str:
        return f"{self.codigo_alumno} - {self.nombres} {self.apellido_paterno} {self.apellido_materno}"
