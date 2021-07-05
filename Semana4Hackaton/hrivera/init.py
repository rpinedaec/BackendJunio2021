
import os
import shutil
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

class Usuario:
    def __init__(self, nombreUsuario, apellidoUsuario, dniUsuario, codUsuario):
        self.nombreUsuario = nombreUsuario
        self.apellidoUsuario = apellidoUsuario
        self.dniUsuario = dniUsuario
        self.codUsuario = codUsuario
    
class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            return file.read()
        except Exception as ex:
            print(ex)
        finally:
            file.close()

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
    

    def toDic(self):
        d = {
            "nombreUsuario": self.nombreUsuario,
            "apellidoUsuario": self.apellidoUsuario,
            "dniUsuario": self.dniUsuario,
            "codUsuario": self.codUsuario
        }
        return d

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

showHome = True
showUsuario = True
showAsistencia = True
showReporte = True
Home_op = {"Usuario": "1", "Asistencia": "2", "Reporte": "3", "Exit": "0"}
usuarioOp = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3", "Listar Usuario": "4" , "Exit": "0"}
asistenciaOp = {"Marcar Fecha y Hora de Entrada": "1", "Marcar Fecha y Hora de Salida": "2", "Exit": "0"}
reporteOp = {"Reporte por Usuario": "1", "Reporte por Fecha": "2", "Exit": "0"}

listaUsuario = []
usuario_listDic = []
fileUsuario = Archivo("Usuario.txt")

Main_menu = Menu("Home", Home_op)
respuesta = Main_menu.show()
while showHome:
    if(respuesta == "0"):
        break
    elif(respuesta == "1"):
        while showUsuario:
            menuUsuario = Menu("Usuario", usuarioOp)
            ansUsuario = menuUsuario.show()
            if(ansUsuario == "0"):
                break
            elif(ansUsuario == "1"):
                nombreUsuario = input("Digite su Nombre: ")
                apellidoUsuario = input("Digite su Apellido: ")
                dniUsuario = input("Digite su D.N.I. : ")
                codUsuario = input("Digite un Codigo de Usuario: ")
                usuario = Usuario(nombreUsuario, apellidoUsuario, dniUsuario, 3)
                listaUsuario.append(usuario)
                usuario_listDic.append(usuario.toDic)
                jsonString = json.dumps(usuario_listDic)
                fileUsuario.borrarArchivo()
                fileUsuario.escribirArchivo(jsonString)
                print("Registrado Nuevo Usuario")
            
            elif(ansUsuario == "2"):
                for lista in listaUsuario:
                    print(lista)
                codigoUsuario = int(input("Escriba su Codigo de Usuario a Buscar: "))
                usuarioEncontrado = None
                for item in listaUsuario:
                    if(item.codUsuario == codigoUsuario):
                        usuarioEncontrado = item
                        break
                if usuarioEncontrado:
                    break
            elif(ansUsuario == "3"):
                break
            elif(ansUsuario == "4"):
                break
    elif(respuesta == "2"):
        while showAsistencia:
            menuAsistencia = Menu("Asistencia", asistenciaOp)
            ansAsistencia = menuAsistencia.show()
            if(ansUsuario == "0"):
                break
            elif(ansAsistencia == "1"):
                break
            elif(ansAsistencia == "2"):
                break
    elif(respuesta == "3"):
        while showReporte:
            menuReporte = Menu("Reporte", reporteOp)
            ansReporte = menuReporte.show()
            if(ansReporte == "0"):
                break
            elif(ansReporte == "1"):
                break
            elif(ansReporte == "2"):
                break
