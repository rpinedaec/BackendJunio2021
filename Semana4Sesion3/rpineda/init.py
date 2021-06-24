import os

class Persona:
    def __init__(self, nombre, sexo, dni):
        self.nombre = nombre
        self.sexo = sexo
        self.dni = dni


class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo 

    def mostrarArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        finally:
            file.close()

    def agregarPersona(self, persona):
        try:
            file = open(self.nombreArchivo, 'a')
            textoAgregar = "{},{},{} \n".format(persona.nombre, persona.sexo, persona.dni)
            file.write(textoAgregar)
        except Exception as ex:
            print(ex)
        finally:
            file.close()
            print(file)


persona = Persona("Karen", "F", 9876)
arch = Archivo("Persona.txt")
arch.agregarPersona(persona)
arch.mostrarArchivo()