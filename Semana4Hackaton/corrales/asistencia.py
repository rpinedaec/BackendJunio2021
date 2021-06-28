#from Semana4Sesion3.rpineda.init import Vendedor
import os
import time
import json

os.system("clear")

print("*************************")
print("*                       *")
print("*   ¡ Bienvenido(@)!    *")
print("*                       *")
print("*************************")

time.sleep(1)

os.system("clear")

print("******************************************")
print("*                                        *")
print("*   ¡Sistema  Control  de Asistencia !   *")
print("*                                        *")
print("******************************************")

print("")
print("")

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

class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, codUsuario = 0):
        super().__init__(nombre, apellido, dni)
        if codUsuario == 0:  
           self.codUsuario = codUsuario + 1
        else:
            self.codUsuario = codUsuario

    def mostrarU(self) -> str:
      return f"{self.nombre} --*-- {self.apellido} --*-- {self.dni} --*-- {self.codUsuario}"
       
#class Asistencia(Persona,Usuario):
    #def __init__(self,nombrePersona, apellidoPersona, dni, nombreUsuario, codUsuario ):
    #    Persona.__init__(self, nombrePersona, apellidoPersona, dni)
    #    Usuario.__init__(self, nombreUsuario, codUsuario)

#Creacion de ARCHIVO
class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    def mostrarArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        finally:
            file.close()

    def agregarUsuario(self, usuario):
        try:
            file = open(self.nombreArchivo, 'a')
            textoAgregar ="{},{},{} \n".format(usuario.nombre, usuario.apellido, usuario.dni, usuario.codUsuario)
            file.write(textoAgregar)
        except Exception as ex:
            print(ex)
        finally:
            file.close()
            print(file)

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
                    #escribir el archivo
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

"""class Menu:
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
                clear()"""


opcion = 0
def menuPrincipal():
    opc = int(input("*** - - - Menu Principal - - - *** \n" +
                    "\n" + 
                    "1. Usuario \n" +
                    "2. Asistencia \n" +
                    "3. Reporte \n" +
                    "4. Salir \n" +
                    "\n" + 
                    "Escoja una Opcion : "))
    return opc

def menuUsuario():
    opc = int(input("**---- Sub Menu Usuario ----**\n" +
                   "\n" + 
                   "1. Agregar Usuario \n" +
                   "2. Buscar Usuario \n" +
                   "3. Quitar Usuario \n" +
                   "4. Listar Usuario \n" +
                   "5. Volver a Menu Principal \n" +
                   "\n" + 
                   "Escoja una Opcion : "))
    return opc

def menuAsistencia():
    opc = int(input("**---- Sub Menu Asistencia ----**\n" +
                    "\n" + 
                    "1. Marcar Fecha y Hora de Entrada \n" +
                    "2. Marcar Fecha y Hora de Salida \n" +
                    "3. Volver a Menu Princiapal \n" +
                    "\n" + 
                    "Escoja una Opcion : "))
    return opc

def menuReporte():
    opc = int(input("**---- Sub Menu Reporte ----**\n" +
                    "\n" +
                    "1. Reporte por Usuario \n" +
                    "2. Reporte por Fecha \n" +
                    "3. Volver a Menu Principal \n" +
                    "\n" +
                    "Escoja una Opcion : "))
    return opc

while opcion != 4:
    
    listaUsuario = []

    opcion = menuPrincipal()
    if(opcion == 1):
        os.system("clear")
        opcion = menuUsuario()
        print("")
        if(opcion == 1):
            nombre = input("Escriba su Nombre: ")
            apellido = input("Escribra su Apellido: ")
            dni = input("Escriba su D.N.I. : ")
            usuario = Usuario(nombre, apellido, dni)
            listaUsuario.append(usuario)
            print(usuario.mostrarU())
            print("Usuario Agregado")
            time.sleep(3)
            os.system("clear")
        
        if(opcion == 2):
            for lista in listaUsuario:
                print(lista)
            codigoUsuario = int(input("Escriba su Codigo de Usuario a Buscar: "))
            usuarioEncontrado = None
            for item in listaUsuario():
                if(item.codUsuario == codigoUsuario):
                   usuarioEncontrado = item
                   print(lista())
                   time.sleep(2)   
                
        elif(opcion == 4):
            break
        if(opcion == 5):   
           print(menuPrincipal)
           os.system("clear")

#Sub Menu de Asistencia
    if opcion == 2:
        os.system("clear")
        opcion = menuAsistencia()
        os.system("clear")
        if opcion == 3:
            os.system("clear")
            print(menuPrincipal)
            os.system("clear")

#Sub Menu de Reposrte      
    if opcion == 3:
        os.system("clear")
        opcion = menuReporte()
        os.system("clear")
        if opcion == 3:
           #menuPrincipal()
           os.system("clear")

#Salir de Sistema
    if opcion == 4:
        os.system("clear")
        print("Hasta, pronto...!Gracias..!")