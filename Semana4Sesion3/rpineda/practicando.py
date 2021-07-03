class Persona:
    def __init__(self, dni, nombre, apellido, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellido= apellido
        self.sexo = sexo
        
persona1 = Persona(43237528, "David", "Alcalde", "M")
print(persona1.dni)

c