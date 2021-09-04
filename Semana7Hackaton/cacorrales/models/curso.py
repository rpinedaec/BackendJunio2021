from conn.conexion import conexionBDD
from conn import conexion
from utils.utils import log
import sys
sys.path.insert(0, '..')

class Curso():
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.curso = {
            "id" : self.id,
            "nombre" : self.nombre
        }

    @staticmethod    
    def insertarCurso(self):
        conn = conexionBDD(4)
        conn.insertarRegistro("curso",self.curso)

    def leerCurso(self): 
        con = conexionBDD(4)
        con.insertarRegistro("curso",'{}')
    
    def actualizarCurso(self):
        con = conexionBDD(4)
        res = con.actualizarRegistro2("curso",self.id,self.curso)
        return(res)