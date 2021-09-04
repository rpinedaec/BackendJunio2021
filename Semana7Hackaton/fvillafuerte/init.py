###########################################
### HACKATON 07 - ADMINISTRADOR NOTAS   ###
### Autor: Franklin Villafuerte Huincho ###
### Fecha: 26/07/2021                   ###
###########################################
import os   
from utils.menu import Menu
from conn.conexion import *
from models.modulos import *

## Menu Coleccion
def mnuColeccion():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Insertar Datos de Ejemplo":"1", "Listar Aulas":"2", "Salir": "0"}
    mnuSec = Menu("COLECCIONES DE EJEMPLO", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertColeccion(conn)
        elif resMSec == "2":
            ListarRegistro(conn,"salon",{},"LISTA DE SALONES")
        elif resMSec == "0":
            bolSWmnu = False

## Menu Profesores
def mnuProfesor():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR PROFESORES", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertProfesor(conn)
        elif resMSec == "2":
            UpdateProfesor(conn)
        elif resMSec == "3":
            DeleteProfesor(conn)
        elif resMSec == "4":
            ListarRegistro(conn,"profesor",{},"LISTA DE PROFESORES")
        elif resMSec == "0":
            bolSWmnu = False

## Menu Profesores
def mnuAlumno():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR ALUMNOS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertAlumno(conn)
        elif resMSec == "2":
            UpdateAlumno(conn)
        elif resMSec == "3":
            DeleteAlumno(conn)
        elif resMSec == "4":
            ListarRegistro(conn,"alumno",{},"LISTA DE ALUMNOS")
        elif resMSec == "0":
            bolSWmnu = False

## Menu cURSOS
def mnuCursos():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR ALUMNOS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertCurso(conn)
        elif resMSec == "2":
            UpdateCurso(conn)
        elif resMSec == "3":
            DeleteCurso(conn)
        elif resMSec == "4":
            ListarRegistro(conn,"curso",{},"LISTA DE CURSOS")
        elif resMSec == "0":
            bolSWmnu = False

## Menu MATRICULAR
def mnuMatricular():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR MATRICULAS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertMatricula(conn)
        elif resMSec == "2":
            UpdateMatricula(conn)
        elif resMSec == "3":
            DeleteMatricula(conn)
        elif resMSec == "4":
            ListarRegistro(conn,"matricula",{},"LISTA DE MATRICULADOS")
        elif resMSec == "0":
            bolSWmnu = False

## Menu REGISTRO DE NOTAS
def mnuRegNotas():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Eliminar Registro":"2", "Listar registro":"3", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR NOTAS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertNota(conn)
        elif resMSec == "2":
            DeleteNota(conn)
        elif resMSec == "3":
            ListarRegistro(conn,"notas_alumno",{},"LISTA DE MATRICULADOS")
        elif resMSec == "0":
            bolSWmnu = False

####################
## Menu Principal ##
####################

conn = conexionBDD(4)

respMenu = "" 
opMainMenu ={"Inicializar Colecciones":"1", "Adm. Profesores":"2", "Adm. Alumnos":"3", "Cursos por Profesor":"4", "Matricular Alumno":"5", "Registrar Notas":"6", "Salir": "0"}
menuPincipal = Menu("Menu Principal - Gestión Notas", opMainMenu) 
bolSW = True
while bolSW:
    respMenu = menuPincipal.show()
    if respMenu == "1":
        mnuColeccion()
    elif respMenu == "2":
        mnuProfesor()
    elif respMenu == "3":
        mnuAlumno()
    elif respMenu == "4":
        mnuCursos()
    elif respMenu == "5":
        mnuMatricular()
    elif respMenu == "6":
        mnuRegNotas()
    elif respMenu == "0":
        bolSW = False
