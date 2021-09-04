import os
from utils.menu import alinear_texto
from utils.utils import *


### INSERTAR COLECCIONES DE EJEMPLO
def InsertColeccion(conn):
    salon = [
        {
            "_id" : 1,
            "nombre" : "PRIMERO A",
            "ano_escolar" : "2021"
        },
        {
            "_id" : 2,
            "nombre" : "PRIMERO B",
            "ano_escolar" : "2021"
        },
        {
            "_id" : 3,
            "nombre" : "SEGUNDO A",
            "ano_escolar" : "2021"
        },
        {
            "_id" : 4,
            "nombre" : "SEGUNDO B",
            "ano_escolar" : "2021"
        }
    ]
    profesor = [
        {
            "_id" : 1,
            "nombre" : "PEREZ GAMARRA ELIAS",
            "edad" : 26,
            "correo" : "elias@gmail.com"
        },
        {
            "_id" : 2,
            "nombre" : "CASAS VIVAS ROXANA",
            "edad" : 32,
            "correo" : "roxi@gmail.com"
        },
        {
            "_id" : 3,
            "nombre" : "CARRASCO VILA GUILLERMO",
            "edad" : 36,
            "correo" : "carrasco@gmail.com"
        }
    ]
    alumno = [
        {
            "_id" : 1,
            "nombre" : "JUAREZ HINOSTROZA IRMA",
            "edad" : 12,
            "correo" : "jhinostroza@gmail.com"
        },
        {
            "_id" : 2,
            "nombre" : "AGUILAR MEJICO JUAN",
            "edad" : 12,
            "correo" : "aguilar25@gmail.com"
        },
        {
            "_id" : 3,
            "nombre" : "GARCIA PORRAS PRCY",
            "edad" : 11,
            "correo" : "garciap@gmail.com"
        },
        {
            "_id" : 4,
            "nombre" : "BRAVO MARTINEZ MARTIN",
            "edad" : 13,
            "correo" : "bravom@gmail.com"
        },
        {
            "_id" : 5,
            "nombre" : "ROSALES MEZA ELIZABETH",
            "edad" : 13,
            "correo" : "rosalesmeza@gmail.com"
        }
    ]

    curso = [
        {
            "_id" : 1,
            "nombre" : "MATEMATICAS 1",
            "id_profesor" : 1
        },
        {
            "_id" : 2,
            "nombre" : "COMUNICACION 1",
            "id_profesor" : 2
        },
        {
            "_id" : 3,
            "nombre" : "MATEMATICAS 2",
            "id_profesor" : 3
        },
        {
            "_id" : 4,
            "nombre" : "COMUNICACION 2",
            "id_profesor" : 2
        }
    ]

    matricula = [
        {
            "_id" : 1,
            "id_alumno" : 1,
            "id_salon" : 1,
            "estado" : "A"
        },
        {
            "_id" : 2,
            "id_alumno" : 2,
            "id_salon" : 1,
            "estado" : "A"
        },
        {
            "_id" : 3,
            "id_alumno" : 3,
            "id_salon" : 1,
            "estado" : "A"
        }
    ]

    notas_alumno = [
        {
            "_id" : 1,
            "id_matricula" : 1,
            "id_curso" : 1,
            "bimestre" : 1,
            "nota" : 12
        },
        {
            "_id" : 2,
            "id_matricula" : 1,
            "id_curso" : 2,
            "bimestre" : 1,
            "nota" : 14
        },
        {
            "_id" : 3,
            "id_matricula" : 2,
            "id_curso" : 1,
            "bimestre" : 1,
            "nota" : 16
        },
        {
            "_id" : 4,
            "id_matricula" : 2,
            "id_curso" : 2,
            "bimestre" : 1,
            "nota" : 15
        }
    ]

    conn.insertarRegistros("salon",salon)
    conn.insertarRegistros("profesor",profesor)
    conn.insertarRegistros("alumno",alumno)
    conn.insertarRegistros("curso",curso)
    conn.insertarRegistros("matricula",matricula)
    conn.insertarRegistros("notas_alumno",notas_alumno)

    input("Se insertó correctamente las coleciones.., presione una tecla para continuar")

def ListarRegistro(conn,coleccion,condi,title):
    os.system('clear')
    print(alinear_texto(title.upper(),40," ","C"))
    print(alinear_texto("",40,"=","C"))
    result = conn.leerRegistros(coleccion,condi)
    for item in result:
        print(item)
    input("Presione una tecla para continuar...")


### FUNCIONES COLECCION PROFESOR
def InsertProfesor(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))

    nombre = input("Apellidos y Nombres: ")
    edad = pedirNumeroEntero("Edad: ")
    correo = input("Correo Electrónico: ")

    id = conn.MaxRegistro("profesor")
    datos = [
        {
            "_id" : id,
            "nombre" : nombre,
            "edad" : edad,
            "correo" : correo
        }
    ]
    result = conn.insertarRegistros("profesor",datos)
    if(result):
        input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateProfesor(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Profesor: ")
    result = conn.leerRegistros("profesor",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1

    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        nombre = input("Apellidos y Nombres: ")
        edad = pedirNumeroEntero("Edad: ")
        correo = input("Correo Electrónico: ")
        result = conn.actualizarRegistro("profesor", {"_id": id_reg}, {"nombre": nombre})
        result = conn.actualizarRegistro("profesor", {"_id": id_reg}, {"edad": edad})
        result = conn.actualizarRegistro("profesor", {"_id": id_reg}, {"correo": correo})
        if(result):
            input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteProfesor(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS PROFESOR",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Profesor a Eliminar: ")
    result = conn.leerRegistros("profesor",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        opc = valOpc()
        if opc == "S":
            result = conn.eliminarRegistro("profesor", {"_id": id_reg} )
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES COLECCION ALUMNO
def InsertAlumno(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))

    nombre = input("Apellidos y Nombres: ")
    edad = pedirNumeroEntero("Edad: ")
    correo = input("Correo Electrónico: ")

    id = conn.MaxRegistro("alumno")
    datos = [
        {
            "_id" : id,
            "nombre" : nombre,
            "edad" : edad,
            "correo" : correo
        }
    ]
    result = conn.insertarRegistros("alumno",datos)
    if(result):
        input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateAlumno(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Alumno: ")
    result = conn.leerRegistros("alumno",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1

    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        nombre = input("Apellidos y Nombres: ")
        edad = pedirNumeroEntero("Edad: ")
        correo = input("Correo Electrónico: ")
        result = conn.actualizarRegistro("alumno", {"_id": id_reg}, {"nombre": nombre})
        result = conn.actualizarRegistro("alumno", {"_id": id_reg}, {"edad": edad})
        result = conn.actualizarRegistro("alumno", {"_id": id_reg}, {"correo": correo})
        if(result):
            input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteAlumno(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS ALUMNO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Alumno a Eliminar: ")
    result = conn.leerRegistros("alumno",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        opc = valOpc()
        if opc == "S":
            result = conn.eliminarRegistro("alumno", {"_id": id_reg} )
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")

### FUNCIONES COLECCION CURSOS
def InsertCurso(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS CURSO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    nombre = input("NOMBRE DEL CURSO: ")
    id_prof = pedirNumeroEntero("ID Profesor: ")
    result = conn.leerRegistros("profesor",{"_id":{"$eq":id_prof}})
    nn = 0
    for item in result:
        print(item['nombre'])
        nn = nn + 1
    if(nn == 0):
        input("No existe ID del Profesor.., presione una tecla para continuar")
    if(nn == 1):
        id = conn.MaxRegistro("curso")
        datos = [
            {
                "_id" : id,
                "nombre" : nombre,
                "id_profesor" : id_prof
            }
        ]
        result = conn.insertarRegistros("curso",datos)
        if(result):
            input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateCurso(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS CURSO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Curso: ")
    result = conn.leerRegistros("curso",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        nombre = input("NOMBRE DEL CURSO: ")
        id_prof = pedirNumeroEntero("ID Profesor: ")
        result = conn.leerRegistros("profesor",{"_id":{"$eq":id_prof}})
        nn = 0
        for item in result:
            print(item['nombre'])
            nn = nn + 1
        if(nn == 0):
            input("No existe ID del Profesor.., presione una tecla para continuar")
        if(nn == 1):
            result = conn.actualizarRegistro("curso", {"_id": id_reg}, {"nombre": nombre})
            result = conn.actualizarRegistro("curso", {"_id": id_reg}, {"id_profesor": id_prof})
            if(result):
                input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteCurso(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS CURSO",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Curso a Eliminar: ")
    result = conn.leerRegistros("curso",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        opc = valOpc()
        if opc == "S":
            result = conn.eliminarRegistro("curso", {"_id": id_reg} )
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES COLECCION MATRICULA
def InsertMatricula(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR DATOS MATRICULA",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_alum = pedirNumeroEntero("ID Alumno: ")
    result = conn.leerRegistros("alumno",{"_id":{"$eq":id_alum}})
    nn = 0
    for item in result:
        print(item['nombre'])
        nn = nn + 1
    if(nn == 0):
        input("No existe ID del Alumno.., presione una tecla para continuar")
    if(nn == 1):
        id_salon = pedirNumeroEntero("ID Salón: ")
        result = conn.leerRegistros("salon",{"_id":{"$eq":id_salon}})
        nn = 0
        for item in result:
            print(item['nombre'])
            nn = nn + 1
        if(nn == 0):
            input("No existe ID del Salón.., presione una tecla para continuar")
        if(nn == 1):
            estado = input("Estado [A]ctivo [I]nactivo: ")
            id = conn.MaxRegistro("matricula")
            datos = [
                {
                    "_id" : id,
                    "id_alumno" : id_alum,
                    "id_salon" : id_salon,
                    "estado" : estado.upper()
                }
            ]
            result = conn.insertarRegistros("matricula",datos)
            if(result):
                input("Se grabó correctamente.., presione una tecla para continuar")

def UpdateMatricula(conn):
    os.system('clear')
    print(alinear_texto("MODIFICAR DATOS MATRICULA",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Matrícula: ")
    result = conn.leerRegistros("matricula",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        id_alum = pedirNumeroEntero("ID Alumno: ")
        result = conn.leerRegistros("alumno",{"_id":{"$eq":id_alum}})
        nn = 0
        for item in result:
            print(item['nombre'])
            nn = nn + 1
        if(nn == 0):
            input("No existe ID del Alumno.., presione una tecla para continuar")
        if(nn == 1):
            id_salon = pedirNumeroEntero("ID Salón: ")
            result = conn.leerRegistros("salon",{"_id":{"$eq":id_salon}})
            nn = 0
            for item in result:
                print(item['nombre'])
                nn = nn + 1
            if(nn == 0):
                input("No existe ID del Salón.., presione una tecla para continuar")
            if(nn == 1):
                estado = input("Estado [A]ctivo [I]nactivo: ")
                result = conn.actualizarRegistro("matricula", {"_id": id_reg}, {"id_alumno": id_alum})
                result = conn.actualizarRegistro("matricula", {"_id": id_reg}, {"id_salon": id_salon})
                result = conn.actualizarRegistro("matricula", {"_id": id_reg}, {"estado": estado.upper()})
                if(result):
                    input("Se actualizó  correctamente.., presione una tecla para continuar")

def DeleteMatricula(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR DATOS MATRICULA",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Matrícula a Eliminar: ")
    result = conn.leerRegistros("matricula",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print(item)
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        print("")
        opc = valOpc()
        if opc == "S":
            result = conn.eliminarRegistro("matricula", {"_id": id_reg} )
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")


### FUNCIONES COLECCION REGISTRO DE NOTAS
def InsertNota(conn):
    os.system('clear')
    print(alinear_texto("REGISTRAR NOTAS",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_mat = pedirNumeroEntero("ID Matricula: ")
    result = conn.leerRegistros("matricula",{"_id":{"$eq":id_mat}})
    nn = 0
    for item in result:
        print('  Estado: ' + item['estado'])
        id_alum = item['id_alumno']
        id_salon = item['id_salon']
        nn = nn + 1
    if(nn == 0):
        input("No existe ID de Matrícula.., presione una tecla para continuar")
    if(nn == 1):
        result = conn.leerRegistros("alumno",{"_id":{"$eq":id_alum}})
        for item in result:
            print('  Alumno: ' + item['nombre'])
        result = conn.leerRegistros("salon",{"_id":{"$eq":id_salon}})
        for item in result:
            print('  Salón: ' + item['nombre'] + ' Año Escolar: ' + item['ano_escolar'])

        id_curso = pedirNumeroEntero("ID Curso: ")
        result = conn.leerRegistros("curso",{"_id":{"$eq":id_curso}})
        nn = 0
        for item in result:
            print('  Curso: ' + item['nombre'])
            id_prof = item['id_profesor']
            nn = nn + 1
        if(nn == 0):
            input("No existe ID del Curso.., presione una tecla para continuar")
        if(nn == 1):
            result = conn.leerRegistros("profesor",{"_id":{"$eq":id_prof}})
            for item in result:
                print('  Profesor: ' + item['nombre'])
            
            bimestre = pedirNumeroEntero("Bimestre (1,2,3,4): ")
            nota = pedirNumeroEntero("Nota(1-20): ")
            id = conn.MaxRegistro("notas_alumno")
            datos = [
                {
                    "_id" : id,
                    "id_matricula" : id_mat,
                    "id_curso" : id_curso,
                    "bimestre" : bimestre,
                    "nota" : nota
                }
            ]
            result = conn.insertarRegistros("notas_alumno",datos)
            if(result):
                input("Se grabó correctamente.., presione una tecla para continuar")


def DeleteNota(conn):
    os.system('clear')
    print(alinear_texto("ELIMINAR NOTAS",40," ","C"))
    print(alinear_texto("",40,"=","C"))
    id_reg = pedirNumeroEntero("ID Reg.Nota: ")
    result = conn.leerRegistros("notas_alumno",{"_id":{"$eq":id_reg}})
    nn = 0
    for item in result:
        print('  Bimestre: ' + str(item['bimestre']))
        print('  NOTA: ' + str(item['nota']))
        id_mat = item['id_matricula']
        id_curso = item['id_curso']
        nn = nn + 1
    if(nn == 0):
        input("No existe ID.., presione una tecla para continuar")
    if(nn == 1):
        result = conn.leerRegistros("matricula",{"_id":{"$eq":id_mat}})
        for item in result:
            id_alum = item['id_alumno']
            id_salon = item['id_salon']

        result = conn.leerRegistros("alumno",{"_id":{"$eq":id_alum}})
        for item in result:
            print('  Alumno: ' + item['nombre'])
        result = conn.leerRegistros("salon",{"_id":{"$eq":id_salon}})
        for item in result:
            print('  Salón: ' + item['nombre'] + ' Año Escolar: ' + item['ano_escolar'])

        result = conn.leerRegistros("curso",{"_id":{"$eq":id_curso}})
        for item in result:
            print('  Curso: ' + item['nombre'])
            id_prof = item['id_profesor']
        result = conn.leerRegistros("profesor",{"_id":{"$eq":id_prof}})
        for item in result:
            print('  Profesor: ' + item['nombre'])

        print("")
        opc = valOpc()
        if opc == "S":
            result = conn.eliminarRegistro("notas_alumno", {"_id": id_reg} )
            if(result):
                input("Se eliminó  correctamente.., presione una tecla para continuar")
