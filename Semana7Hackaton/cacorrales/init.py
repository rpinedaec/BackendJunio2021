from time import sleep
from pymongo import MongoClient
from pymongo.results import InsertManyResult
from utils.utils import log
from utils.utils import Menu, color
from conn.conexion import conexionBDD
from models.alumno import Alumno
from models.profesor import Profesor
from models.curso import Curso
from models.salon import Salon
from pprint import pprint
from tabulate import TableFormat, tabulate


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
        if(ansMenu == "1"):
            id = input("Escribe el ID Profesor: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe DNI : ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            objProfesor = Profesor(id,nombre,dni,edad,correo)
            res = Profesor.insertarProfesor(objProfesor)      
            print(res)
            input("presiona cualquier tecla para continuar...")
    
 #--- Listar Profesor---#
        elif(ansMenu == "2"):
            print("Lista Profesores")
            print("")
            con = conexionBDD(4)
            res = con.leerRegistros2("profesor")
            #header = res[0].keys()
            lis_rest = [x for x in res]
            #print(tabulate(lis_rest, headers=header, tablefmt='fancy_grid'))
            pprint(lis_rest)
            input("presiona cualquier tecla para continuar")
        
  #--- Actualizar Profesor---#
        elif(ansMenu == "3"):
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            objProfesor = Profesor(id,nombre,dni,edad,correo)
            resul = Profesor.actualizarProfesor(objProfesor)  
            if(resul):
                print("Se modifico correctamente")
                print("")
                input("presiona una tecla para continuar...")

  #--- Buscar Profesor---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            con = conexionBDD(4)
            res = con.leerRegistro("profesor",{"id":str(codigo)})
            print(res)
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
            id = input("Escribe tu ID Alumno: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe DNI : ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            objAlumno = Alumno(id,nombre,dni,edad,correo)
            res = Alumno.insertarAlumno(objAlumno)      
            print(res)
            input("presiona cualquier tecla para continuar...")
                    
  #--- Listar Alumno---#
        elif(ansMenu == "2"):
            print("Lista Alumnos")
            print("")
            con = conexionBDD(4)
            res = con.leerRegistros2("alumno")
            #header = res[0].keys()
            lis_rest = [x for x in res]
            #print(tabulate(lis_rest, headers=header, tablefmt='fancy_grid'))
            pprint(lis_rest)
            input("presiona cualquier tecla para continuar")

  #--- Actualizar Alumno---#
        elif(ansMenu == "3"):
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            objAlumno = Alumno(id,nombre,dni,edad,correo)
            resul = Alumno.actualizarProfesor(objAlumno)  
            if(resul):
                print("Se modifico correctamente")
                print("")
                input("presiona una tecla para continuar...")

  #--- Buscar Alumno---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            con = conexionBDD(4)
            res = con.leerRegistro("alumno",{"id":str(codigo)})
            print(res)
            input("presiona cualquier tecla para continuar...")    

def menuCurso():
    opMenu = {"Crear Curso": "1", "Listar Curso": "2", "Actualizar Curso": "3", "Buscar Curso": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Curso", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break
  #--- Crear Curso---#
        if(ansMenu == "1"):
            idcurso = input("Escribe tu ID Curso: ")
            nombre = input("Escribe nombre Curso: ")
            codcurso = input("Escribe CodCurso : ")
            objCurso = Curso(idcurso,nombre,codcurso)
            res = Curso.insertarCurso(objCurso)      
            print(res)
            input("presiona cualquier tecla para continuar...")
            
  #--- Listar Curso---#
        elif(ansMenu == "2"):
            print("Lista Profesores")
            print("")
            con = conexionBDD(4)
            res = con.leerRegistros2("profesor")
            #header = res[0].keys()
            lis_rest = [x for x in res]
            #print(tabulate(lis_rest, headers=header, tablefmt='fancy_grid'))
            pprint(lis_rest)
            input("presiona cualquier tecla para continuar")
        
  #--- Actualizar Curso---#
        elif(ansMenu == "3"):
            id = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            dni = input("Escribe tu DNI: ")
            edad = input("Escribe tu edad: ")
            correo = input("Escribe tu email: ")
            objProfesor = Profesor(id,nombre,dni,edad,correo)
            resul = Profesor.actualizarProfesor(objProfesor)  
            if(resul):
                print("Se modifico correctamente")
                print("")
                input("presiona una tecla para continuar...")   

  #--- Buscar Curso---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            con = conexionBDD(4)
            res = con.leerRegistro("profesor",{"id":str(codigo)})
            print(res)
            input("presiona cualquier tecla para continuar...")    


def menuSalon():
    opMenu = {"Crear Salon": "1", "Listar Salon": "2", "Actualizar Salon": "3", "Buscar Salon": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("Salon", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break
#--- Crear Salon---#
        if(ansMenu == "1"):
            idsalon = input("Escribe tu ID Salon: ")
            nombre = input("Escribe nombre Salon: ")
            anoescolar = input("Escribe CodSalon : ")
            codsalon = input("Escribe CodSalon : ")
            idprofesor_profesor = input("Escribe el IdProfesor : ")
            idalumno_alumno = input("Esribe el IdAlumno")
            objSalon = Salon(idsalon,nombre,anoescolar,codsalon,idprofesor_profesor,idalumno_alumno)
            res = Salon.insertarSalon(objSalon)      
            print(res)
            input("presiona cualquier tecla para continuar...")
            
  #--- Listar Salon---#
        elif(ansMenu == "2"):
            print("Lista Salon")
            print("")
            con = conexionBDD(4)
            res = con.leerRegistros2("salon")
            #header = res[0].keys()
            lis_rest = [x for x in res]
            #print(tabulate(lis_rest, headers=header, tablefmt='fancy_grid'))
            pprint(lis_rest)
            input("presiona cualquier tecla para continuar")
        
  #--- Actualizar Salon---#
        elif(ansMenu == "3"):
            idsalon = input("escoje un ID para modificar: ")
            nombre = input("Escribe tu nombre: ")
            anoescolar = input("Escribe Año Escolar: ")
            codsalon = input("Escribe Salon: ")
            idprofesor_profesor = input("Escribe Id Profesor: ")
            idalumno_alumno = input("Escribe Id Alumno: ")
            objSalon = Salon(idsalon,nombre,anoescolar,codsalon,idprofesor_profesor,idalumno_alumno)
            resul = Salon.actualizarProfesor(objSalon)  
            if(resul):
                print("Se modifico correctamente")
                print("")
                input("presiona una tecla para continuar...")

  #--- Buscar Curso---#
        elif(ansMenu == "4"):
            codigo = int(input("Ingresa el ID a buscar: "))
            con = conexionBDD(4)
            res = con.leerRegistro("salon",{"idsalon":str(codigo)})
            print(res)
            input("presiona cualquier tecla para continuar...")    

try:
    opMenuPrincipal = {"Menu Profesores": "1", "Menu Alumnos": "2","Menu Cursos": "3","Menu Salon":"4","Salir": "0"}
    showHome = True
    ansMenuPrincipal = ""
    menuPrincipal = Menu("Principal", opMenuPrincipal)
    while showHome:
        ansMenuPrincipal = menuPrincipal.show()
        if(ansMenuPrincipal == "0"):
            break
        elif(ansMenuPrincipal == "1"):
            menuProfesor()
        elif(ansMenuPrincipal == "2"):
            menuAlumnos()
        elif(ansMenuPrincipal == "3"):
            menuCurso()
        elif(ansMenuPrincipal == "4"):
            menuSalon()
except Exception as error:
    sleep(2)
    print(str(error))