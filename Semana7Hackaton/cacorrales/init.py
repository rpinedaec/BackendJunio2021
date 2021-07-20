from time import time

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

#lstAlumnos = []
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
           id = input("Escriba el ID Alumno: ")
           nombre = input("Escribe tu nombre: ")
           dni = input("Escribe DNI : ")
           edad = input("Escribe tu edad: ")
           correo = input("Escribe tu email: ")
           result = Alumno(id,nombre,dni,edad,correo)
           result.append(insert)
           if result:      
                conn = conexionBDD(4)
                conn.insertarRegistro(Alumno,result())
                print("Error")
                input("presiona cualquier tecla para continuar...")
        
        except Exception as err:
            log.error(err)



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
    #time(2)
    print(str(error))