import sys
sys.path.insert(0, '..')
from utils.utils import log
from models.persona import Persona

class Alumno(Persona):
    def __init__(self,nombre,dni,edad,correo):
          super().__init__(nombre, dni, edad, correo)
          self.id = id
   #def __str__(self) -> str:
   #     return f"{self.id} {self.nombre} {self.dni} {self.edad} {self.correo}"

   # @staticmethod
    def toCollection(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "dni": self.dni,
            "edad": self.edad,
            "correo": self.correo
        }
    
    
    #def ingresarAlumno(notas):
    #    alumnos = []
    #    thislog = log("ingresar")
    #    for i in notas:
    #        thislog.debug(i.notas)
    #        listaNotas = i.notas
    #        promedio = sum(listaNotas)/len(listaNotas)
    #        insert = {
    #        'alumno': i.nombre,
    #        'notas' : listaNotas,
    #        'notaMinima': min(listaNotas),
    #        'notaMaxima': max(listaNotas),
    #        'promedio':promedio
    #        }
    #        alumnos.append(insert)
    #    if alumnos:      
    #        conn = conexionBDD(4)
    #        conn.insertarRegistros("notas",alumnos)