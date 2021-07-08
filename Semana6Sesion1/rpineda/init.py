#import psycopg2 

# try:
#     conn = connect(user='postgres',
#                                password="pachaqtec2021",
#                                host="localhost",
#                                port="5432",
#                                database="colegio")
#     cur = conn.cursor()
#     query = """
#     insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
# values ('P0001','Renato','Valdez','Vega',35,'rvaldez@colegio.com');
#     """
#     cur.execute(query)
#     conn.commit()
#     # record = cur.fetchall()
#     # print(record)
# except Error as error:
#     print(f"Hubo un error: {str(error)}")
# finally:
#     if(conn):
#         cur.close()
#         conn.close()

from conexion import conexion
from tabulate import tabulate
import os
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#class Profesor:
#    def __init__(self,codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email):
#        self.codigo_profesor = codigo_profesor
#        self.nombres = nombres
#        self.apellido_paterno = apellido_paterno
#        self.apellido_materno = apellido_materno
#        self.edad = edad
#        self.email = email
#----------------------------------------------------------------------------------------------

class Alumno:
    def __init__(self, codigo_alumno, nombres, apellido_paterno,apellido_materno ,edad, correo,direccion):
        self.codigo_alumno = codigo_alumno
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.correo = correo
        self.direccion = direccion

class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(key + color.GREEN + " → " + color.END + value)
            print("")
            ans = input(
                color.YELLOW + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED + "Opción no valida, escoja una opción valida" + color.END)
                time.sleep(3)
        return ans

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()

conn = conexion()
opMenuPrincipal ={"Crear Alumno":"1", "Listar Alumno":"2", "Actualizar Alumno":"3", "Salir": "0"}
showHome = True
ansMenuPrincipal = "" 
menuPincipal = Menu("Menu Principal", opMenuPrincipal) 
while showHome:
    ansMenuPrincipal = menuPincipal.show()
    if(ansMenuPrincipal == "0"):
        break
    elif(ansMenuPrincipal == "1"):
        codigo = input("Escribe el Codigo del Alumno: ")
        nombre = input("Escribe tu nombre: ")
        apellidoPaterno= input("Escribe tu apellido Paterno: ")
        apellidoMaterno= input("Escribe tu apellido Materno: ")
        edad= input("Escribe tu edad: ")
        email = input("Escribe tu email: ")
        direccion = input("Escribe tu Direccion: ")
        query = f"""insert into alumnos (id_alumno,codigo_alumno,nombres,apellido_paterno,apellido_materno,edad,correo,direccion) 
                values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}',{edad},'{email}','{direccion}');"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")
    elif(ansMenuPrincipal == "2"):
        query = """Select * from alumnos"""
        result = conn.consultarBDD(query)
        header = ['ID', 'Codigo', 'Nombre', 'Ape - Paterno', 'Ape - Materno', 'Edad', 'Telefono', 'Direccion', 'Email','Profesion']
       # print(result)
        print(tabulate(result, headers=header,showindex=True, tablefmt='fancy_grid'))
        input("presiona cualquier tecla para continuar")
    elif(ansMenuPrincipal == "3"):
        query = """Select * from alumnos"""
        result = conn.consultarBDD(query)
        print(color.RED +"|Id\t\t|Codigo\t|Nombre"+ color.END)
        for item in result:
            print(f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|{item[5]}\t|")
        id = input("escoje un ID para modificar: ")
        codigo = input("Escribe el Codigo del ID Alumno: ")
        nombre = input("Escribe tu nombre: ")
        apellidoPaterno= input("Escribe tu apellido Paterno: ")
        apellidoMaterno= input("Escribe tu apellido Materno: ")
        edad= input("Escribe tu edad: ")
        email = input("Escribe tu email: ")
        direccion = input("Escribe tu Direccion: ")
        query = f"""update alumnos
                    set codigo_alumno = '{codigo}',
                    nombres = '{nombre}',
                    apellido_paterno = '{apellidoPaterno}',
                    apellido_materno = '{apellidoMaterno}',
                    edad = {edad},
                    email = '{email}'
                    direccion ='{direccion}'
                    where id_profesor = {id};"""
        result = conn.ejecutarBDD(query)
        if(result):
            print("Se ejecuto correctamente")
        input("presiona una tecla para continuar...")

#----------------------------------------------------------------------------#


#opMenuPrincipal ={"Crear Profesor":"1", "Listar Profesor":"2", "Actualizar Profesor": "3", "Salir": "0"}
#showHome = True
#ansMenuPrincipal = "" 
#menuPincipal = Menu("Menu Principal", opMenuPrincipal) 
#while showHome:
#    ansMenuPrincipal = menuPincipal.show()
#    if(ansMenuPrincipal == "0"):
#        break
#    elif(ansMenuPrincipal == "1"):
#        codigo = input("Escribe el Codigo del Profe: ")
#        nombre = input("Escribe tu nombre: ")
#        apellidoPaterno= input("Escribe tu apellido Paterno: ")
#        apellidoMaterno= input("Escribe tu apellido Materno: ")
#        edad= input("Escribe tu edad: ")
#        email = input("Escribe tu email: ")
#        query = f"""insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
#                values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}',{edad},'{email}');"""
#        result = conn.ejecutarBDD(query)
#        if(result):
#            print("Se ejecuto correctamente")
#    elif(ansMenuPrincipal == "2"):
#        query = """Select * from profesores"""
#        result = conn.consultarBDD(query)
#        header = ['ID', 'Codigo', 'Nombre', 'Paterno', 'Materno', 'Edad', 'Telefono', 'Direccion', 'Email','Profesion']
#       # print(result)
#        print(tabulate(result, headers=header,showindex=True, tablefmt='fancy_grid'))
#        input("presiona cualquier tecla para continuar")
#    elif(ansMenuPrincipal == "3"):
#        query = """Select * from profesores"""
#        result = conn.consultarBDD(query)
#        print(color.RED +"|Id\t\t|Codigo\t|Nombre"+ color.END)
#        for item in result:
#            print(f"|{item[0]}\t|{item[1]}\t|{item[2]}\t|{item[3]}\t|{item[4]}\t|{item[5]}\t|")
#        id = input("escoje un ID para modificar: ")
#        codigo = input("Escribe el Codigo del Profe: ")
#        nombre = input("Escribe tu nombre: ")
#        apellidoPaterno= input("Escribe tu apellido Paterno: ")
#        apellidoMaterno= input("Escribe tu apellido Materno: ")
#        edad= input("Escribe tu edad: ")
#        email = input("Escribe tu email: ")
#        email = input("Escribe tu email: ")
#        query = f"""update profesores
#       #            set codigo_profesor = '{codigo}',
       #            nombres = '{nombre}',
       #            apellido_paterno = '{apellidoPaterno}',
       #            apellido_materno = '{apellidoMaterno}',
       #            edad = {edad},
       #            email = '{email}'
       #            where id_profesor = {id};"""
       # result = conn.ejecutarBDD(query)
       # if(result):
       #     print("Se ejecuto correctamente")
       # input("presiona una tecla para continuar...")

# query = """insert into profesores (codigo_profesor,nombres,apellido_paterno,apellido_materno,edad,email) 
# values ('P0003','Paul','Vega','Espinoza',35,'pvega@colegio.com');"""

# conn = conexion()
# # result = conn.ejecutarBDD(query)
# # print (result)

# query = """Select * from profesores"""
# result = conn.consultarBDD(query)
# print(result)