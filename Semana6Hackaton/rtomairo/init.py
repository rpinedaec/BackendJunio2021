from conexion import conexion
from utils import Menu, color
from models.usuarios import *
from tabulate import tabulate
from validacion import *

conn = conexion()
lstProfesores = []
lstAlumnos = []

def mostrarRegistro(tabla):
    if tabla =='profesor' or tabla=="alumno":
        query = f"""Select * from {tabla};"""
        result = conn.consultarBDD(query)
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['ID', 'Nombre', 'Dni', 'Edad','Email']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    elif tabla == 'cursoprofesor':
        query = f"""select p.nombre, p.edad, p.correo, c.nombre as curso
                from cursoprofesor 
                inner join profesor p
                on cursoprofesor.profesor_id = p.id
                inner join curso c
                on cursoprofesor.curso_id = c.id;"""
        result = conn.consultarBDD(query)
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['nombre de profesor', 'edad', 'correo', 'curso']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    elif tabla=='curso':
        query = f"""Select * from {tabla};"""
        result = conn.consultarBDD(query)
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['ID', 'Nombre']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    elif tabla =='periodo':
        query = f"""Select * from {tabla};"""
        result = conn.consultarBDD(query)
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['ID', 'Nombre','Año','Bimestre']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    elif tabla=='salon':
        query = f"""select s.nombre as salon, p.nombre as Profesor, 
                a.nombre as Alumno, per.nombre as Periodo, 
                b.nombre as Bimestre
                from salon s
                inner join profesor p
                on s.profesor_id = p.id
                inner join alumno a
                on s.alumno_id = a.id
                inner join periodo per
                on s.periodo_id = per.id
                inner join bimestre b
                on per.id = b.id;"""
        result = conn.consultarBDD(query)
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['Salon', 'Profesor', 'Alumno', 'Periodo','Bimestre']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
    
def actualizarRegistros(tabla):
    query = f"""Select * from {tabla}"""
    result = conn.consultarBDD(query)
    if tabla =='profesor' or tabla=="alumno":
        print(color.GREEN + f"{tabla.upper()}" + color.GREEN)
        header = ['ID', 'Nombre', 'Dni', 'Edad','Correo']
        print(tabulate(result, headers=header, tablefmt='fancy_grid'))
        id = input("escoje un ID para modificar: ")
        id = validarNum(id)
        nombre = input("Escribe tu nombre y apellidos: ")
        dni = input("Escribe tu DNI: ")
        dni = validarDNI(dni)#? observar
        edad = input("Escribe tu edad: ")
        edad = validarNum(edad)
        correo = input("Escribe tu correo: ")
        query = f"""update {tabla}
                    set nombre = '{nombre}',
                    dni = '{dni}',
                    edad = '{edad}',
                    correo = '{correo}'
                    where id = {id};"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")    



def ingresarRegistro(tabla):
    if tabla =='profesor' or tabla=="alumno":
        nombre = input("Escribe tu nombre: ")
        edad = input("Escribe tu edad: ")
        edad = validarNum(edad)
        dni = input("Escribe tu DNI: ")
        dni = validarDNI(dni)#? observar
        correo = input("Escribe tu email: ")
        query = f"""insert into {tabla} values (DEFAULT,'{nombre}','{dni}','{edad}','{correo}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")
    if tabla=='curso':
        nombre = input("Escribe nombre del curso: ")
        query = f"""insert into {tabla} values (DEFAULT,'{nombre}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")
    if tabla =="periodo":
        nombre = input("Escribe nombre del periodo: ")
        anio = input("Escribe el año del periodo: ")
        anio = validarNum(anio)
        idBimestre = input("Escribe 1 o 2 si es primer o segundo bimestre: ")
        idBimestre=validarNum(idBimestre)
        query = f"""insert into {tabla} values (DEFAULT,'{nombre}','{anio}','{idBimestre}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")
    if tabla=="salon":
        nombre = input("Escribe nombre del Salon: ")
        idPeriodo = input("Escribe el ID del periodo: ")
        idPeriodo=validarNum(idPeriodo)
        profesorID = input("Escribe el ID del Profesor: ")
        profesorID=validarNum(profesorID)
        alumnoID = input("Escribe el ID del Alumno: ")
        alumnoID=validarNum(alumnoID)
        query = f"""insert into {tabla} values (DEFAULT,'{nombre}','{idPeriodo}','{profesorID}','{alumnoID}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")

def cargaInicial():
    query = """Select * from profesor;"""
    result = conn.consultarBDD(query)
    for item in result:
        newProfesor = Profesor(item[0], item[1], item[2], item[3], item[4])
        lstProfesores.append(newProfesor)
    query = """Select * from alumno;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newAlumno = Alumno(item[0], item[1], item[2], item[3],item[4])
        lstAlumnos.append(newAlumno)
def menuProfesores():
    opMenuProfesor = {"Crear Profesor": "1", "Listar Profesor": "2",
                      "Actualizar Profesor": "3", "Buscar Profesor": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menuProfesores = Menu("Profesores", opMenuProfesor)
    while showMenu:
        ansMenu = menuProfesores.show()
        if(ansMenu == "0"):
            break
        if(ansMenu == "1"):
            ingresarRegistro('profesor')
            input("presiona cualquier tecla para continuar")

        elif(ansMenu == "2"):
            mostrarRegistro('profesor')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "3"):
            actualizarRegistros('profesor')
            input("presiona una tecla para continuar...")
        elif(ansMenu == "4"):
            DNI = input("Ingresa el DNI a buscar: ")
            DNI = validarDNI(DNI)         
            for item in lstProfesores:
                if(item.dni == DNI):
                    print(color.PURPLE + f"{item}" + color.PURPLE)
                    input("presiona cualquier tecla para continuar...")
                    break


def menuAlumnos():
    opMenuAlumno = {"Crear Alumno": "1", "Listar Alumno": "2",
                      "Actualizar Alumno": "3", "Buscar Alumno": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menuAlumnos = Menu("Alumnos", opMenuAlumno)
    while showMenu:
        ansMenu = menuAlumnos.show()
        if(ansMenu == "0"):
            break
        if(ansMenu == "1"):
            ingresarRegistro('alumno')
            input("presiona cualquier tecla para continuar")

        elif(ansMenu == "2"):
            mostrarRegistro('alumno')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "3"):
            actualizarRegistros('alumno')
            input("presiona una tecla para continuar...")
        elif(ansMenu == "4"):
            DNI = input("Ingresa el DNI a buscar: ")
            DNI = validarDNI(DNI)           
            for item in lstAlumnos:
                if(item.dni == DNI):
                    print(color.PURPLE + f"{item}" + color.PURPLE)
                    input("presiona cualquier tecla para continuar...")
                    break

def menuCursos():
    opMenuCurso = {"Crear Curso": "1", "Listar Cursos": "2",
                      "Curso dictor por Profesores": "3", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menuCurso = Menu("Cursos", opMenuCurso)
    while showMenu:
        ansMenu = menuCurso.show()
        if(ansMenu == "0"):
            break
        if(ansMenu == "1"):
            ingresarRegistro('curso')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "2"):
            mostrarRegistro('curso')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "3"):
           mostrarRegistro('cursoprofesor')
           input("presiona cualquier tecla para continuar")


def menuPeriodo():
    opMenuP = {"Crear Periodo": "1", "Mostrar Periodo academico": "2","Salir": "0"}
    showMenu = True
    ansMenu = ""
    menuP = Menu("Cursos", opMenuP)
    while showMenu:
        ansMenu = menuP.show()
        if(ansMenu == "0"):
            break
        if(ansMenu == "1"):
            ingresarRegistro('periodo')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "2"):
            mostrarRegistro('periodo')
            input("presiona cualquier tecla para continuar")



def menuSalon():
    opMenuS = {"Crear Salon": "1", "Mostrar Salon": "2","Salir": "0"}
    showMenu = True
    ansMenu = ""
    menuS = Menu("Cursos", opMenuS)
    while showMenu:
        ansMenu = menuS.show()
        if(ansMenu == "0"):
            break
        if(ansMenu == "1"):
            ingresarRegistro('salon')
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "2"):
            mostrarRegistro('salon')
            input("presiona cualquier tecla para continuar")

cargaInicial()


try:
    opMenuPrincipal = {"Menu Profesores": "1", "Menu Alumnos": "2","Menu Cursos":"3","Menu Salon":"4" ,"Menu Periodo":"5","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        elif(ansMenuPrincipal == "1"):
            menuProfesores()
        elif(ansMenuPrincipal == "2"):
            menuAlumnos()
        elif(ansMenuPrincipal == "3"):
            menuCursos()
        elif(ansMenuPrincipal == "4"):
            menuSalon()
        elif(ansMenuPrincipal == "5"):
            menuPeriodo()
except Exception as error:
    print(str(error))