#from Semana4Sesion3.rpineda.init import Vendedor
import os
import time
import json

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

class Persona:
    def __init__(self, nombre,apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    def mostrarP(self) -> str:
        return f"{self.nombre} -- {self.apellido} -- {self.dni}"

class Usuario:
    def __init__(self, nombreUsuario, codUsuario):
        self.nombreUsuario = nombreUsuario
        self.codUsuario= codUsuario
    def mostrarU(self) -> str:
        return f"{self.nombreUsuario} -- {self.codUsuario}"
       
class Asistencia(Persona,Usuario):
    def __init__(self,nombrePersona, apellidoPersona, dni, nombreUsuario, codUsuario ):
        Persona.__init__(self, nombrePersona, apellidoPersona, dni)
        Usuario.__init__(self, nombreUsuario, codUsuario)

class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()
        except Exception as e:
            return e
        

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        print(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                print("removiendo archivo")

            except Exception as error:
                print(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            print(error)      

    # def agregarPersona(self, persona):
    #     try:
    #         file = open(self.nombreArchivo, 'a')
    #         textoAgregar = "{},{},{} \n".format(persona.nombre, persona.sexo, persona.dni)
    #         file.write(textoAgregar)
    #     except Exception as ex:
    #         print(ex)
    #     finally:
    #         file.close()
    #         print(file)

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
                print("Hasta, pronto...!Gracias..!")
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
showHome = True
opMenuPrincipal = {"Usuario":"1","Asistencia":"2", "Reporte":"3", "Salir":"0"}
ansMenuPrincipal = ""
menuPrincipal = Menu("Menu Principal", opMenuPrincipal)
#--Sub Menu Usuario --#
opSubMenuUsuario = {"Agregar Usuario":"1","Buscar Usuario":"2","Quitar Usuario":"3","Listar Usuario":"4","Salir de Sub Menu Usuario":"0"}
ansSubMenuUsuario =""
menuUsuaio = Menu( "Sub Menu Usuario", opSubMenuUsuario )

while showHome:
    ansMenuPrincipal = menuPrincipal.show()
    if(ansMenuPrincipal == "0"):
        break
    elif(ansMenuPrincipal == "1"):

        print("Sub Menu de Usuario")
        
    elif(ansMenuPrincipal == "2"):
        print("Sub Menu Marcado de Asistencia")
    elif(ansMenuPrincipal == "3"):
        print("Sub Menu de Reportes")

