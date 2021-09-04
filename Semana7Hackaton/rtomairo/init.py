from models.alumno import Alumno
from models.profesor import Profesor
from utils.utils import log
from utils.utils import Menu
from conn.conexion import conexionBDD
import time

listAlumno = []
listAlumnoDic = []
listProfesor = []
listProfesorDic = []
def CargarDatos():
    conn = conexionBDD(1)
    condicion = {}
    registrosAlumno = conn.leerRegistros("Alumno",condicion)
    registrosProfesor = conn.leerRegistros("Profesor",condicion)
    for value in registrosAlumno:
        newAlumno = Alumno(value['codigo'],value['nombre'],value['ape_paterno'],value['ape_materno'],value['dni'],value['edad'],value['correo'])
        listAlumno.append(newAlumno)
        listAlumnoDic.append(newAlumno.todic())

    for value in registrosProfesor:
        newProfesor = Profesor(value['codigo'],value['nombre'],value['ape_paterno'],value['ape_materno'],value['dni'],value['edad'],value['correo'])
        listProfesor.append(newProfesor)
        listProfesorDic.append(newProfesor.todic())


CargarDatos()
log = log("Inicio")
log.info("Inicio de la aplicacion")




def InsertandoAlumnos():
    log.debug("Ingresando alumnos")
    codigo = input("Ingrese el codigo: ")
    nombre=input("Ingrese el nombre: ")
    apellidop= input("Ingrese el apellido paterno: ")
    apellidom=input("Ingrese el apellido materno: ")
    dni=input("Ingrese DNI: ")
    edad =input("Ingrese la edad: ")
    correo=input("Ingrese el correo: ")
    alumno = Alumno(codigo,nombre,apellidop,apellidom,dni,edad,correo)
    listAlumno.append(alumno)
    res = Alumno.ingresarAlumno(listAlumno)

def InsertandoProfesores():
    log.debug("Ingresando Profesor")
    codigo = input("Ingrese el codigo: ")
    nombre=input("Ingrese el nombre: ")
    apellidop= input("Ingrese el apellido paterno: ")
    apellidom=input("Ingrese el apellido materno: ")
    dni=input("Ingrese DNI: ")
    edad =input("Ingrese la edad: ")
    correo=input("Ingrese el correo: ")
    profesor = Profesor(codigo,nombre,apellidop,apellidom,dni,edad,correo)
    listProfesor.append(profesor)
    res = Profesor.ingresarProfesor(listProfesor)

def BuscarRegistro():
    log.debug("Buscando alumnos")
    dni = input("Ingrese el DNI: ")
    for lista in listAlumnoDic:
        if lista['dni'] ==dni:
            AlumnoEncontrado = lista
            print(f"codigo: {AlumnoEncontrado['codigo']} {AlumnoEncontrado['nombre']} {AlumnoEncontrado['ape_paterno']} {AlumnoEncontrado['ape_materno']} - {AlumnoEncontrado['dni']}")

def BuscarRegistroP():
    log.debug("Buscando Profesores")
    dni = input("Ingrese el DNI: ")
    for lista in listProfesorDic:
        if lista['dni'] ==dni:
            ProfesorEncontrado = lista
            print(f"codigo: {ProfesorEncontrado['codigo']} {ProfesorEncontrado['nombre']} {ProfesorEncontrado['ape_paterno']} {ProfesorEncontrado['ape_materno']} - {ProfesorEncontrado['dni']}")

def MostrarRegistros():
    log.debug("Mostrando alumnos")
    conn = conexionBDD(1)
    consulta = {}
    registroAl = conn.leerRegistros("Alumno",consulta)
    for value in registroAl:
        print(f"{value['codigo']} - {value['nombre']} {value['ape_paterno']} {value['ape_materno']} {value['dni']}")

def MostrarRegistrosP():
    log.debug("Mostrando Profesores")
    conn = conexionBDD(1)
    consulta = {}
    registroAl = conn.leerRegistros("Profesor",consulta)
    for value in registroAl:
        print(f"{value['codigo']} - {value['nombre']} {value['ape_paterno']} {value['ape_materno']} {value['dni']}")

def EliminarRegistro():
    log.debug("Eliminando alumno")
    dni = input("Ingrese el DNI: ")
    for lista in listAlumnoDic:
        if lista['dni'] ==dni:
            AlumnoEncontrado = lista
            conn = conexionBDD(1)
            conn.eliminarRegistro("Alumno",AlumnoEncontrado)

 
def EliminarRegistroP():
    log.debug("Eliminando profesor")
    dni = input("Ingrese el DNI: ")
    for lista in listProfesorDic:
        if lista['dni'] ==dni:
            ProfesorEncontrado = lista
            conn = conexionBDD(1)
            conn.eliminarRegistro("Profesor",ProfesorEncontrado)           
            
def ActualizarRegistros():
    log.debug("Actualizando alumnos")
    dni = input("Ingrese el DNI: ")
    for lista in listAlumnoDic:
        if lista['dni'] ==dni:
            AlumnoEncontrado = lista
            codigo = input("Ingrese el codigo: ")
            nombre=input("Ingrese el nombre: ")
            apellidop= input("Ingrese el apellido paterno: ")
            apellidom=input("Ingrese el apellido materno: ")
            dni=input("Ingrese DNI: ")
            edad =input("Ingrese la edad: ")
            correo=input("Ingrese el correo: ")
            alumno = Alumno(codigo,nombre,apellidop,apellidom,dni,edad,correo)
            conn = conexionBDD(1)
            conn.actualizarRegistro("Alumno",AlumnoEncontrado,alumno.todic())


def ActualizarRegistrosP():
    log.debug("Actualizando profesores")
    dni = input("Ingrese el DNI: ")
    for lista in listProfesorDic:
        if lista['dni'] ==dni:
            ProfesorEncontrado = lista
            codigo = input("Ingrese el codigo: ")
            nombre=input("Ingrese el nombre: ")
            apellidop= input("Ingrese el apellido paterno: ")
            apellidom=input("Ingrese el apellido materno: ")
            dni=input("Ingrese DNI: ")
            edad =input("Ingrese la edad: ")
            correo=input("Ingrese el correo: ")
            profesor = Profesor(codigo,nombre,apellidop,apellidom,dni,edad,correo)
            conn = conexionBDD(1)
            conn.actualizarRegistro("Profesor",ProfesorEncontrado,profesor.todic())

def MenuAlumnos():
    showAlumno = True
    OpmenuAlumno ={"Ingresar Alumno:":"1","Buscar Alumno:":"2","Eliminar Alumno:":"3","Actualizar Alumno:":"4", "Mostrar Alumnos":5}
    menAlumno = "Menu de alummnos"
    mAlumno = Menu(menAlumno,OpmenuAlumno)
    respuestaAl=mAlumno.mostrarMenu()
    # log=log("Inicio")
    while showAlumno:
        if(respuestaAl==0):
            break
            showAlumno=False
        elif(respuestaAl ==1):
            InsertandoAlumnos()
            print("Alumno Agregado")
            time.sleep(8)
            break
        elif(respuestaAl ==2):
            BuscarRegistro()
            # print(resConn)
            time.sleep(4)
            break
        elif(respuestaAl ==3):
            EliminarRegistro()
            print("Alumno se ha borrado")
            time.sleep(4)
            break
        elif(respuestaAl ==4):
            ActualizarRegistros()
            print("Se realizo los cambios")
            time.sleep(4)
            break
        elif (respuestaAl ==5):
            MostrarRegistros()
            time.sleep(4)
            break
def MenuProfesores():
    showProfesor = True
    OpmenuP ={"Ingresar Profesor:":"1","Buscar Profesor:":"2","Eliminar Profesor:":"3","Actualizar Profesor:":"4", "Mostrar Profesor":5}
    menP = "Menu de alummnos"
    mProfesor = Menu(menP,OpmenuP)
    respuestaAl=mProfesor.mostrarMenu()
    # log=log("Inicio")
    while showProfesor:
        if(respuestaAl==0):
            break
            showAlumno=False
        elif(respuestaAl ==1):
            InsertandoProfesores()
            print("Profesor Agregado")
            time.sleep(8)
            break
        elif(respuestaAl ==2):
            BuscarRegistroP()
            # print(resConn)
            time.sleep(4)
            break
        elif(respuestaAl ==3):
            EliminarRegistroP()
            print("Alumno se ha borrado")
            time.sleep(4)
            break
        elif(respuestaAl ==4):
            ActualizarRegistrosP()
            print("Se realizo los cambios")
            time.sleep(4)
            break
        elif (respuestaAl ==5):
            MostrarRegistrosP()
            time.sleep(4)
            break

def MenuMain():
    showHome = True
    OpListaO ={"Alumnos:":"1","Profesores:":"2","Cursos:":"3","Salon:":"4"}
    menuName = "Menu Principal"
    menuPrincipal = Menu(menuName,OpListaO)
    respuesta=menuPrincipal.mostrarMenu()
    while showHome:
        if(respuesta ==0):
            showHome=False
        elif(respuesta ==1):
            MenuAlumnos()
        elif(respuesta==2):
            MenuProfesores()

MenuMain()