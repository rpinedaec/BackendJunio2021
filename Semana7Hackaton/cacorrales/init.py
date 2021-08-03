from time import sleep
from pymongo import MongoClient
from pymongo.results import InsertManyResult
from utils.utils import log
from utils.utils import Menu, color
from models.persona import Persona
#from models.profesor import Profesor
from models.alumno import Alumno
#from models.curso import Curso
#from models.salon import Salon
#from tabulate import TableFormat, tabulate
from conn.conexion import conexionBDD

log = log("Inicio")
log.info("Inicio de la aplicacion")


#-------- Profesor --------#

def menuProfesor():
    opMenu = {"Crear Profesor": "1", "Listar Profesor": "2", "Actualizar Profesor": "3", "Buscar Profesor": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Profesor", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break
  #--- Crear Profesor---#
        try: 
           id = input("Escribe el ID Profesor: ")
           nombre = input("Escribe tu nombre: ")
           dni = input("Escribe DNI : ")
           edad = input("Escribe tu edad: ")
           correo = input("Escribe tu email: ")
           objAlumno = Alumno(id,nombre,dni,edad,correo)
           res = Alumno.insertarAlumno(objAlumno)      
           print(res)
           input("presiona cualquier tecla para continuar...")
        except Exception as err:
           log.error(err)

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
        try: 
           id = input("Escribe tu ID Alumno: ")
           nombre = input("Escribe tu nombre: ")
           dni = input("Escribe DNI : ")
           edad = input("Escribe tu edad: ")
           correo = input("Escribe tu email: ")
           objAlumno = Alumno(id,nombre,dni,edad,correo)
           res = Alumno.insertarAlumno(objAlumno)      
           print(res)
           input("presiona cualquier tecla para continuar...")
        except Exception as err:
           log.error(err)
            
  #--- Listar Alumno---#
       # elif(ansMenu == "2"):
       #query = """Select * from alumno"""
       # result = conn.consultarBDD(query)
       # header = ['ID','Nombre Apellido', 'dni','Edad', 'Correo Electronico']
       # print(tabulate(result, headers=header, tablefmt='fancy_grid'))
        #print("")
        #input("presiona cualquier tecla para continuar")
        
  #--- Actualizar Alumno---#
        #elif(ansMenu == "3"):
        #query = """Select * from alumno"""
        #result = conn.consultarBDD(query)
        #header = ['ID','Nombre','DNI','Edad','Correo Electronico']
        #print(tabulate(result,headers=header,tablefmt='fancy_grid'))
        #id = input("escoje un ID para modificar: ")
        #nombre = input("Escribe tu nombre: ")
        #dni = input("Escribe tu DNI: ")
        #edad = input("Escribe tu edad: ")
        #correo = input("Escribe tu email: ")
        #query = f"""update alumno set nombre = '{nombre}',dni = '{dni}',edad = {edad},correo = '{correo}'
        #             where id = {id};"""
        #result = conn.ejecutarBDD(query)
        #if(result):
        #    print("Se modifico correctamente")
        #    print("")
        #    input("presiona una tecla para continuar...")

  #--- Buscar Alumno---#
        #elif(ansMenu == "4"):
        #    codigo = int(input("Ingresa el ID a buscar: "))
        #    for item in lstAlumnos:
        #        if(item.id == codigo):
        #            print(item)
        #            input("presiona cualquier tecla para continuar...")




#cargaInicial()

try:
    opMenuPrincipal = {"Menu Profesores": "1", "Menu Alumnos": "2","Menu Cursos": "3","Menu Salon":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        #elif(ansMenuPrincipal == "1"):
            #menuProfesores()
        elif(ansMenuPrincipal == "2"):
            menuAlumnos()
        #elif(ansMenuPrincipal == "3"):
            #menuCurso()
        #elif(ansMenuPrincipal == "4"):
            #menuSalon()
except Exception as error:
    sleep(2)
    print(str(error))