from conexion import conexion
from utils import Menu, color
from profesor import Profesor
from alumno import Alumno
from tabulate import tabulate
from curso import Curso

conn = conexion()
lstProfesores = []
lstAlumnos = []
lstCurso = []


def cargaInicial():
    # - - Carga Inicial Tabla Profesor - - #
    query = """Select * from profesor;"""
    result = conn.consultarBDD(query)
    for item in result:
        newProfesor = Profesor(
            item[1], item[2], item[3], item[4])
        lstProfesores.append(newProfesor)
   
    # - - Carga Inicial Tabla Alumno - - #
    query = """Select * from alumno;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newAlumno = Alumno(item[1], item[2], item[3], item[4])
        lstAlumnos.append(newAlumno)

    # - - Carga Inicial Tabla Curso - - #
    query = """Select * from curso;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newCurso = Curso(item[1], item[2])
        lstCurso.append(newCurso)


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
        #--- Crear ---#
        if(ansMenu == "1"):
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""insert into profesor (nombre, dni, edad, correo) 
                    values ('{nombre}','{dni}','{edad}','{correo}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newProfesor = Profesor(nombre, dni, edad, correo)
                lstProfesores.append(newProfesor)
                print("Se guardo correctamente la informacion.!")
        
        #--- Listar ---#
        elif(ansMenu == "2"):
            query = """Select * from profesor"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre','dni','Edad','Correo Electronico']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar ---#
        elif(ansMenu == "3"):
            query = """Select * from profesor"""
            result = conn.consultarBDD(query)
            print(color.RED + "|Id\t|Nombre Apellido\t|DNI...   \t|Edad\t|Correo Electronico" + color.END)
            for item in result:
                print(
                    f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|")
            print("")
            id = int(input("escoje un DNI para modificar a Profesor: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""update profesor
                        set nombre = '{nombre}',dni = '{dni}',edad = {edad}, correo = '{correo}'
                        where dni = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("Se ejecuto actualizò correctamente")
            input("presiona una tecla para continuar...")
        
        #--- Buscar ---#
        elif(ansMenu == "4"):
            codigo = input("Ingresa el DNI del Profesor a buscar: ")
            for item in lstProfesores:
                if(item.dni == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")

#-------- Alumno --------#

def menuAlumnos():
    opMenu = {"Crear Alumno": "1", "Listar Alumno": "2",
                      "Actualizar Alumno": "3", "Buscar Alumno": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Alumnos", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break

         #--- Crear ---#
        if(ansMenu == "1"):
            #codigo = input("Escribe el Codigo del Alumno: ")
            nombre = input("Escribe tu nombre: ")
            #apellidoPaterno = input("Escribe tu apellido Paterno: ")
            #apellidoMaterno = input("Escribe tu apellido Materno: ")
            dni = input("Escribe DNI : ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            #direccion = input("Escribe la direccion: ")
            query = f"""insert into alumno (nombre,dni,edad,correo) 
                    values ('{nombre}','{dni}','{edad}','{correo}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newAlumno = Alumno(nombre, dni, edad, correo)
                lstAlumnos.append(newAlumno)
                print("Se creo nuevo Alumno correctamente")
            else:
                print("Error")
                input("presiona cualquier tecla para continuar...")

        #--- Listar ---#
        elif(ansMenu == "2"):
            query = """Select * from alumno"""
            result = conn.consultarBDD(query)
            header = ['ID','Nombre Apellido', 'dni','Edad', 'Correo Electronico']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            input("presiona cualquier tecla para continuar")
        
        #--- Actualizar ---#
        elif(ansMenu == "3"):
            query = """Select * from alumno"""
            result = conn.consultarBDD(query)
            print(color.RED + "|Id\t\t|Codigo\t|Nombre" + color.END)
            for item in result:
                print(
                    f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|")
            id = input("escoje un DNI para modificar: ")
            #codigo = input("Escribe el Codigo del Profe: ")
            nombre = input("Escribe tu nombre: ")
            #apellidoPaterno = input("Escribe tu apellido Paterno: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            query = f"""update alumno set nombre = '{nombre}',dni = '{dni}',edad = {edad},correo = '{correo}'
                        where dni = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("Se ejecuto Actualizo correctamente")
            input("presiona una tecla para continuar...")

        #--- Buscar ---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el DNI a buscar: "))
            for item in lstAlumnos:
                if(item.dni == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")


cargaInicial()

try:
    opMenuPrincipal = {"Menu Profesores": "1", "Menu Alumnos": "2", "Salir": "0"}
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
except Exception as error:
    print(str(error))