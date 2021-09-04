
class Profesor:
    def __init__(self,codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,telefono, direccion,email, profesion):
        self.codigo_profesor = codigo_profesor
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.profesion = profesion
    
    def __str__(self) -> str:
        return f"{self.codigo_profesor} - {self.nombres} {self.apellido_paterno} {self.apellido_materno}"
