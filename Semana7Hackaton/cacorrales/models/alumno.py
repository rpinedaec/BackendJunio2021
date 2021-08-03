from conn.conexion import conexionBDD
from conn import conexion
from utils.utils import log
import sys
sys.path.insert(0, '..')

class Alumno:
    def __init__(self, id, nombre, dni, edad, correo):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
        self.alumno = {
            "id": self.id,
            "nombre": self.nombre,
            "dni": self.dni,
            "edad": self.edad,
            "correo": self.correo
        }

    @staticmethod
    def insertarAlumno(self):
        conn = conexionBDD(4)
        conn.insertarRegistro("alumno",self.alumuno)
     
    def leerAlumno(self):   
        con = conexionBDD(4)
        con.insertarRegistro("alumno",'{}')
    
    def actualizarAlumno(self):
        con = conexionBDD(4)
        res = con.actualizarRegistro2("alumno",self.id,self.alumno)
        return(res)