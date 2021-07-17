from re import S
from time import time
from conexion import conexion
from utils import Menu, color
from profesor import Profesor
from alumno import Alumno
from curso import Curso
from salon import Salon
from tabulate import TableFormat, tabulate

conn = conexion()
lstProfesores = []
lstAlumnos = []
lstCurso = []
lstSalon = []

def cargaInicial():
    # - - Carga Inicial Tabla Profesor - - #
    query = """Select * from profesor;"""
    result = conn.consultarBDD(query)
    for item in result:
        newProfesor = Profesor(item[0], item[1], item[2], item[3],item[4])
        lstProfesores.append(newProfesor)
   
    # - - Carga Inicial Tabla Alumno - - #
    query = """Select * from alumno;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newAlumno = Alumno(item[0],item[1], item[2], item[3], item[4])
        lstAlumnos.append(newAlumno)

    # - - Carga Inicial Tabla Curso - - #
    query = """Select * from curso;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newCurso = Curso(item[0], item[1])
        lstCurso.append(newCurso)
    
    # -- Carga Inicial Tabla Salon -- #
    query = """Select * from salon;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newSalon = Salon(item[0], item[1], item[2], item[3], item[4])
        lstSalon.append(newSalon)


#-------- Profesor --------#

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

        #--- Crear Profesor ---#
        if(ansMenu == "1"):
            id = (0)
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""insert into profesor (nombre, dni, edad, correo) values ('{nombre}','{dni}','{edad}','{correo}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newProfesor = Profesor( id, nombre, dni, edad, correo)
                lstProfesores.append(newProfesor)
                print("")
                print("Se guardo correctamente la informacion.!")
        
        #--- Listar Profesor ---#
        elif(ansMenu == "2"):
            query = """Select * from profesor"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre','DNI','Edad','Correo Electronico']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            print("")
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar Profesor---#
        elif(ansMenu == "3"):
            query = """Select * from profesor"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre','DNI','Edad','Correo Electronico']
            print(tabulate(result,headers=header,tablefmt='fancy_grid'))
            #print(color.RED + "|Id\t|Nombre Apellido\t|DNI...   \t|Edad\t|Correo Electronico" + color.END)
            #for item in result:
            #    print(
            #        f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|")
            id = int(input("escoje el ID para modificar a Profesor: "))
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""update profesor
                        set nombre = '{nombre}',dni = '{dni}',edad = {edad}, correo = '{correo}'
                        where id = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("")
                print("Se modifico correctamente")
                print("")
            input("presiona una tecla para continuar...")
        
        #--- Buscar Profesor---#
        elif(ansMenu == "4"):
            codigo =input("Ingresa el DNI del Profesor a buscar: ")
            for item in lstProfesores:
                if(item.dni == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")

#-------- Alumno --------#

def menuAlumnos():
    opMenu = {"Crear Alumno": "1", "Listar Alumno": "2", "Actualizar Alumno": "3", "Buscar Alumno": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Alumnos", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break

         #--- Crear Alumno---#
        if(ansMenu == "1"):
            id = (0)
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe DNI : ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""insert into alumno (nombre,dni,edad,correo) values ('{nombre}','{dni}','{edad}','{correo}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newAlumno = Alumno(id, nombre, dni, edad, correo)
                lstAlumnos.append(newAlumno)
                print("Se creo nuevo Alumno correctamente")
            else:
                print("Error")
                input("presiona cualquier tecla para continuar...")

        #--- Listar Alumno---#
        elif(ansMenu == "2"):
            query = """Select * from alumno"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre Apellido', 'dni','Edad', 'Correo Electronico']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            print("")
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar Alumno---#
        elif(ansMenu == "3"):
            query = """Select * from alumno"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre','DNI','Edad','Correo Electronico']
            print(tabulate(result,headers=header,tablefmt='fancy_grid'))
            #print(color.RED + "|Id\t|Nombre\t|DNI\t|Edad\t|Correo Electronico" + color.END)
            #for item in result:
            #    print(
            #        f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|")
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""update alumno set nombre = '{nombre}',dni = '{dni}',edad = {edad},correo = '{correo}'
                        where id = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("Se modifico correctamente")
                print("")
            input("presiona una tecla para continuar...")

        #--- Buscar Alumno---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            for item in lstAlumnos:
                if(item.id == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")


#-------- Curso --------#

def menuCurso():
    opMenu = {"Crear Curso": "1", "Listar Curso": "2",
                      "Actualizar Curso": "3", "Buscar Curso": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Cursos", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break

         #--- Crear Curso---#
        if(ansMenu == "1"):
            id = (0)
            nombre = input("Escribe nombre del Curso: ")
            query = f"""insert into curso (nombre) values ('{nombre}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newCurso = Curso(id, nombre)
                lstCurso.append(newCurso)
                print("")
                print("Se creo nuevo Curso correctamente")
            else:
                print("Error")
                input("presiona cualquier tecla para continuar...")

        #--- Listar Curso ---#
        elif(ansMenu == "2"):
            query = """Select * from curso"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre Curso']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            print("")
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar Curso ---#
        elif(ansMenu == "3"):
            query = """Select * from curso"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre']
            print(tabulate(result,headers=header,tablefmt='fancy_grid'))
            #print(color.RED + "|Id\t|Nombre" + color.END)
            #for item in result:
            #    print(
            #        f"|{item[0]}\t|{item[1]}\t|")
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            query = f"""update curso set nombre = '{nombre}'
                        where id = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("")
                print("Se actualizo correctamente")
                print("")
            input("presiona una tecla para continuar...")

        #--- Buscar Curso ---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            for item in lstCurso:
                if(item.id == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")

#-------- Salon --------#

def menuSalon():
    opMenu = {"Crear Salon": "1", "Listar Salon": "2", 
                "Actualizar Salon": "3", "Buscar Salon": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Salon", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break

 #--- Crear Salon---#
        if(ansMenu == "1"):
            id = (0)
            nombre = input("Escribe nombre del Salon : ")
            periodo_id = input("Escriba el ID Periodo : ")
            profesor_id = input("Escriba el ID Profesor : ")
            alumno_id = input("Escriba el ID Alumno : ")
            query = f"""insert into salon (nombre,periodo_id,profesor_id,alumno_id) values ('{nombre}','{periodo_id}','{profesor_id}','{alumno_id}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newSalon = Salon(id, nombre,periodo_id,profesor_id,alumno_id)
                lstSalon.append(newSalon)
                print("")
                print("Se creo nuevo Salon correctamente")
            else:
                print("Error")
                input("presiona cualquier tecla para continuar...")

        #--- Listar Salon ---#
        elif(ansMenu == "2"):
            query = """Select * from salon"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre Salon','Periodo_ID','Profesor_ID','Alumno_ID']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            print("")
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar Salon ---#
        elif(ansMenu == "3"):
            query = """Select * from salon"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre Salon','Periodo_ID','Profesor_ID','Alumno_ID']
            print(tabulate(result,headers=header,tablefmt='fancy_grid'))
            #print(color.RED + "|Id\t|Nombre" + color.END)
            #for item in result:
            #    print(
            #        f"|{item[0]}\t|{item[1]}\t|")
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe nombre salon : ")
            query = f"""update curso set nombre = '{nombre}',periodo_id = '{periodo_id}',profesor_id = {profesor_id},alumno_id = '{alumno_id}'
                        where id = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("")
                print("Se actualizo correctamente")
                print("")
            input("presiona una tecla para continuar...")

        #--- Buscar Salon ---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID de Salon a buscar: "))
            for item in lstSalon:
                if(item.id == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")

cargaInicial()

try:
    opMenuPrincipal = {"Menu Profesores": "1", "Menu Alumnos": "2","Menu Cursos": "3","Menu Salon":"4","Salir": "0"}
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
            menuCurso()
        elif(ansMenuPrincipal == "4"):
            menuSalon()
except Exception as error:
    time(2)
    print(str(error))