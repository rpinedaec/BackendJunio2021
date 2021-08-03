from conn.conexion import conexionBDD
from conn import conexion
from utils.utils import log
from bson.objectid import ObjectId
import json
#from models.persona import Persona
import sys
sys.path.insert(0, '..')

class Alumno:
    def __init__(self, id, nombre, dni, edad, correo):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo

    @staticmethod
    def insertarAlumno(self):
        alumno = []
        insert = {
            "id": self.id,
            "nombre": self.nombre,
            "dni": self.dni,
            "edad": self.edad,
            "correo": self.correo
        }

        conn = conexionBDD(4)
        conn.insertarRegistro("alumno",insert)