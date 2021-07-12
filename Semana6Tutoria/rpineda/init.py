from conexion import conexion
from utils import Menu, color
from profesor import Profesor
from alumno import Alumno
from tabulate import tabulate

conn = conexion()
lstProfesores = []
lstAlumnos = []


def cargaInicial():
    query = """Select * from profesor;"""
    result = conn.consultarBDD(query)
    for item in result:
        newProfesor = Profesor(
            item[1], item[2], item[3], item[4])
        lstProfesores.append(newProfesor)
    query = """Select * from alumno;"""
    result = conn.consultarBDD(query)
    print(result)
    for item in result:
        newAlumno = Alumno(item[1], item[2], item[3], item[4])
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
            codigo = input("Escribe el Codigo del Profe: ")
            nombre = input("Escribe tu nombre: ")
            apellidoPaterno = input("Escribe tu apellido Paterno: ")
            apellidoMaterno = input("Escribe tu apellido Materno: ")
            edad = input("Escribe tu edad: ")
            telefono = input("Escribe el telefono: ")
            direccion = input("Escribe la direccion: ")
            email = input("Escribe tu email: ")
            profesion = input("Escribe la profesion: ")
            query = f"""insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,telefono,direccion,email,profesion) 
                    values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}',{edad},'{telefono}','{direccion}','{email}', '{profesion}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newProfesor = Profesor(codigo, nombre, apellidoPaterno,
                                       apellidoMaterno, edad, telefono, direccion, email, profesion)
                lstProfesores.append(newProfesor)
                print("Se ejecuto correctamente")

        elif(ansMenu == "2"):
            query = """Select * from profesores"""
            result = conn.consultarBDD(query)
            header = ['ID', 'Codigo', 'Nombre', 'Paterno', 'Materno',
                      'Edad', 'Telefono', 'Direccion', 'Email', 'Profesion']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "3"):
            query = """Select * from profesores"""
            result = conn.consultarBDD(query)
            print(color.RED + "|Id\t\t|Codigo\t|Nombre" + color.END)
            for item in result:
                print(
                    f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|{item[5]}\t|")
            id = input("escoje un ID para modificar: ")
            codigo = input("Escribe el Codigo del Profe: ")
            nombre = input("Escribe tu nombre: ")
            apellidoPaterno = input("Escribe tu apellido Paterno: ")
            apellidoMaterno = input("Escribe tu apellido Materno: ")
            edad = input("Escribe tu edad: ")
            email = input("Escribe tu email: ")
            query = f"""update profesores
                        set codigo_profesor = '{codigo}',
                        nombres = '{nombre}',
                        apellido_paterno = '{apellidoPaterno}',
                        apellido_materno = '{apellidoMaterno}',
                        edad = {edad},
                        email = '{email}'
                        where id_profesor = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("Se ejecuto correctamente")
            input("presiona una tecla para continuar...")
        elif(ansMenu == "4"):
            codigo = input("Ingresa el codigo a buscar: ")
            for item in lstProfesores:
                if(item.codigo_profesor == codigo):
                    print(item)
                    input("presiona cualquier tecla para continuar...")


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
        if(ansMenu == "1"):
            codigo = input("Escribe el Codigo del Alumno: ")
            nombre = input("Escribe tu nombre: ")
            apellidoPaterno = input("Escribe tu apellido Paterno: ")
            apellidoMaterno = input("Escribe tu apellido Materno: ")
            edad = input("Escribe tu edad: ")
            email = input("Escribe tu email: ")
            direccion = input("Escribe la direccion: ")
            query = f"""insert into alumnos (codigo_alumno,nombres,apellido_paterno,apellido_materno,edad,correo,direccion) 
                    values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}','{edad}','{email}','{direccion}');"""
            result = conn.ejecutarBDD(query)

            if(result):
                newAlumno = Alumno(codigo, nombre, apellidoPaterno,
                                       apellidoMaterno, edad,email, direccion)
                lstAlumnos.append(newAlumno)
                print("Se ejecuto correctamente")
            else:
                print("Error")
                input("presiona cualquier tecla para continuar...")

        elif(ansMenu == "2"):
            query = """Select * from alumnos"""
            result = conn.consultarBDD(query)
            header = ['ID', 'Codigo', 'Nombre', 'Paterno', 'Materno',
                      'Edad', 'Email', 'Direccion']
            print(tabulate(result, headers=header, tablefmt='fancy_grid'))
            input("presiona cualquier tecla para continuar")
        elif(ansMenu == "3"):
            query = """Select * from profesores"""
            result = conn.consultarBDD(query)
            print(color.RED + "|Id\t\t|Codigo\t|Nombre" + color.END)
            for item in result:
                print(
                    f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|{item[5]}\t|")
            id = input("escoje un ID para modificar: ")
            codigo = input("Escribe el Codigo del Profe: ")
            nombre = input("Escribe tu nombre: ")
            apellidoPaterno = input("Escribe tu apellido Paterno: ")
            apellidoMaterno = input("Escribe tu apellido Materno: ")
            edad = input("Escribe tu edad: ")
            email = input("Escribe tu email: ")
            query = f"""update profesores
                        set codigo_profesor = '{codigo}',
                        nombres = '{nombre}',
                        apellido_paterno = '{apellidoPaterno}',
                        apellido_materno = '{apellidoMaterno}',
                        edad = {edad},
                        email = '{email}'
                        where id_profesor = {id};"""
            result = conn.ejecutarBDD(query)
            if(result):
                print("Se ejecuto correctamente")
            input("presiona una tecla para continuar...")
        elif(ansMenu == "4"):
            codigo = input("Ingresa el codigo a buscar: ")
            for item in lstProfesores:
                if(item.codigo_profesor == codigo):
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
