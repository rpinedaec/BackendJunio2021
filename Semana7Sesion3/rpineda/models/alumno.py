import sys
sys.path.insert(0, '..')
from utils.utils import log
from conn.conexion import conexionBDD

class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    @staticmethod
    def ingresarAlumno(notas):
        alumnos = []
        thislog = log("ingresar")
        for i in notas:
            thislog.debug(i.notas)
            listaNotas = i.notas
            promedio = sum(listaNotas)/len(listaNotas)
            insert = {
                'alumno': i.nombre,
                'notas' : listaNotas,
                'notaMinima': min(listaNotas),
                'notaMaxima': max(listaNotas),
                'promedio':promedio
            }
            alumnos.append(insert)
        if alumnos:      
            conn = conexionBDD(4)
            conn.insertarRegistros("notas",alumnos)