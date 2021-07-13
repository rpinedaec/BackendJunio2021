###########################################
### HACKATON 06 - ADMINISTRADOR NOTAS   ###
### Autor: Franklin Villafuerte Huincho ###
### Fecha: 12/07/2021                   ###
###########################################
import os   
from models.menu import Menu
from paquete.modulos import *
from conexion import conexion

## Menu Salones
def mnuSalon():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("ADMINISTRAR SALONES", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertSalon(conn)
        elif resMSec == "2":
            UpdateSalon(conn)
        elif resMSec == "3":
            DeleteSalon(conn)
        elif resMSec == "4":
            query = """select * from salon;"""
            header = ['ID', 'SALON', 'AÑO ESCOLAR']
            ListarRegistro(conn,header,query,"LISTA DE SALONES")
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
            query = """select * from profesor;"""
            header = ['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO']
            ListarRegistro(conn,header,query,"LISTA DE PROFESORES")
        elif resMSec == "0":
            bolSWmnu = False

## Menu Alumnos
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
            query = """select * from alumno;"""
            header = ['ID', 'APELLIDOS Y NOMBRES', 'EDAD', 'CORREO']
            ListarRegistro(conn,header,query,"LISTA DE ALUMNOS")
        elif resMSec == "0":
            bolSWmnu = False


## Menu Cursos por Profesor
def mnuCursos():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("CURSOS POR PROFESOR", opMnuSec) 
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
            query = """select a.*,b.nombre as profesor from curso as a inner join profesor as b on a.id_profesor=b.id_profesor;"""
            header = ['ID CURSO', 'CURSO', 'ID PROF.', 'PROFESOR']
            ListarRegistro(conn,header,query,"LISTA DE CURSOS POR PROFESOR")
        elif resMSec == "0":
            bolSWmnu = False

## Menu Cursos por Salón
def mnuCursosSalon():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Eliminar Registro":"2", "Listar registro":"3", "Salir": "0"}
    mnuSec = Menu("CURSOS POR SALON", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertCursoSalon(conn)
        elif resMSec == "2":
            DeleteCursoSalon(conn)
        elif resMSec == "3":
            query = """select a.id_salon,b.nombre as salon,a.id_curso,c.nombre as curso, case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest from salon_cursos as a inner join salon as b on a.id_salon=b.id_salon inner join curso as c on a.id_curso=c.id_curso order by a.id_salon;"""
            header = ['ID SALON', 'SALON', 'ID CURSO.', 'CURSO', 'ESTADO']
            ListarRegistro(conn,header,query,"LISTA DE CURSOS POR SALON")
        elif resMSec == "0":
            bolSWmnu = False


## Menu Matricular
def mnuMatricular():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Modificar Registro":"2", "Eliminar Registro":"3", "Listar registro":"4", "Salir": "0"}
    mnuSec = Menu("MATRICULA DE ALUMNOS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertMatricula(conn)
        if resMSec == "2":
            UpdateMatricula(conn)
        elif resMSec == "3":
            DeleteMatricula(conn)
        elif resMSec == "4":
            query = """select a.id_matricula,c.nombre as salon,b.nombre as alumno,case a.estado when 'A' then 'Activo' else 'Inactivo' end as cest from matricula as a inner join alumno as b on a.id_alumno=b.id_alumno inner join salon as c on a.id_salon=c.id_salon order by salon,alumno;"""
            header = ['ID MATRICULA', 'SALON', 'ALUMNO', 'ESTADO']
            ListarRegistro(conn,header,query,"LISTA DE CURSOS POR SALON")
        elif resMSec == "0":
            bolSWmnu = False

## Menu Matricular
def mnuRegNotas():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Registro":"1", "Eliminar Registro":"2", "Listar registro":"3", "Salir": "0"}
    mnuSec = Menu("MATRICULA DE ALUMNOS", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            InsertRegNotas(conn)
        elif resMSec == "2":
            DeleteRegNotas(conn)
        elif resMSec == "3":
            query = """select a.id_matricula,d.nombre as salon,c.nombre as alumno,f.nombre as profesor,e.nombre as curso,g.nombre as bimestre,a.nota from notas_alumno as a inner join matricula as b on a.id_matricula=b.id_matricula inner join alumno as c on b.id_alumno=c.id_alumno inner join salon as d on b.id_salon=d.id_salon inner join curso as e on a.id_curso=e.id_curso inner join profesor as f on e.id_profesor=f.id_profesor inner join bimestre as g on a.id_bimestre=g.id_bimestre ORDER BY salon,alumno,curso;"""
            header = ['ID MATRICULA', 'SALON', 'ALUMNO', 'PROFESOR', 'CURSO', 'BIMESTRE', 'NOTA']
            ListarRegistro(conn,header,query,"LISTA DE CURSOS POR SALON")
        elif resMSec == "0":
            bolSWmnu = False

####################
## Menu Principal ##
####################

conn = conexion()
respMenu = "" 
opMainMenu ={"Adm. Salón":"1", "Adm. Profesores":"2", "Adm. Alumnos":"3", "Cursos por Profesor":"4", "Cursos por Salón":"5", "Matricular Alumno":"6", "Registrar Notas":"7", "Salir": "0"}
menuPincipal = Menu("Menu Principal - Gestión Notas", opMainMenu) 
bolSW = True
while bolSW:
    respMenu = menuPincipal.show()
    if respMenu == "1":
        mnuSalon()
    elif respMenu == "2":
        mnuProfesor()
    elif respMenu == "3":
        mnuAlumno()
    elif respMenu == "4":
        mnuCursos()
    elif respMenu == "5":
        mnuCursosSalon()
    elif respMenu == "6":
        mnuMatricular()
    elif respMenu == "7":
        mnuRegNotas()
    elif respMenu == "0":
        bolSW = False
