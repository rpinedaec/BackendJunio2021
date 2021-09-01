from conn.conexion import conexionBDD
from conn import conexion
from utils.utils import log
import sys
sys.path.insert(0, '..')

class Salon():
    def __init__(self,id,nombre,periodo_id,profesor_id,alumno_id):
          self.id = id
          self.nombre = nombre
          self.periodo_id = periodo_id
          self.profesor_id = profesor_id
          self.alumno_id = alumno_id
          self.salon = {
              "id" : self.id,
              "nombre" : self.nombre,
              "periodo_id" : self.periodo_id,
              "profesor_id" : self.profesor_id,
              "alumno_id" : self.alumno_id             
          }

    @staticmethod
    def insertarSalon(self):
        conn = conexionBDD(4)
        conn.insertarRegistro("salon",'{}')
    
    def leerSalon(self):
        conn = conexionBDD(4)
        conn.insertarRegistro("salon",'{}')
    
    def actualizarSalon(self):
        con = conexionBDD(4)
        res = con.actualizarRegistro2("salon",self.id,self.salon)
        return(res)