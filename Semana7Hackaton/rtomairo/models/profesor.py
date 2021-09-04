import sys
sys.path.insert(0, '..')
from utils.utils import log
from conn.conexion import conexionBDD

class Profesor:
    def __init__(self,codigo ,nombre, ape_paterno,ape_materno,dni, edad, correo):
        self.codigo= codigo
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.dni = dni
        self.edad = edad
        self.correo = correo
    def __str__(self):
        return f"{self.nombre} - {self.ape_paterno} {self.ape_materno}"
    @staticmethod
    def ingresarProfesor(datos):
        profesores = []
        thislog = log("ingresar")
        for i in datos:
            thislog.debug(datos)
            insert ={
            'codigo':i.codigo,
            'nombre':i.nombre,
            'ape_paterno':i.ape_paterno,
            'ape_materno':i.ape_materno,
            'dni':i.dni,
            'edad':i.edad,
            'correo':i.correo
        }
        profesores.append(insert)
        if profesores:
            conn = conexionBDD(1)
            conn.insertarRegistro("Profesor",insert)
    # @staticmethod
    def todic(self):
        d ={
            'codigo':self.codigo,
            'nombre':self.nombre,
            'ape_paterno':self.ape_paterno,
            'ape_materno':self.ape_materno,
            'dni':self.dni,
            'edad':self.edad,
            'correo':self.correo
        }
        return d