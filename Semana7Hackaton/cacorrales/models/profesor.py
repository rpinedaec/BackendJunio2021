from conn.conexion import conexionBDD
from conn import conexion
from utils.utils import log
import sys
sys.path.insert(0, '..')

class Profesor:
    def __init__(self, id, nombre, dni, edad, correo):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.correo = correo
        self.profesor = {
            "id": self.id,
            "nombre": self.nombre,
            "dni": self.dni,
            "edad": self.edad,
            "correo": self.correo
        }
    
    @staticmethod
    def insertarProfesor(self):
        conn = conexionBDD(4)
        conn.insertarRegistro("profesor",self.profesor)
    
    def leerProfesor(self):
        con = conexionBDD(4)
        con.leerRegistros("profesor",'{}')
    
    def actualizarProfesor(self):
        con = conexionBDD(4)
        res = con.actualizarRegistro2("profesor",self.id,self.profesor)
        return(res)