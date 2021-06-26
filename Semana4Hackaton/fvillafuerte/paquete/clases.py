import os
import time
from paquete.modulos import alinear_texto

### CLASE MENU ###
class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print(alinear_texto("",40,"-","C"))
            print(alinear_texto(self.name.upper(),40,":","C"))
            print(alinear_texto("",40,"-","C"))
            print("")
            for (key, value) in self.op_list.items():
                print("[" + value + "] " + key)
            print("")
            ans = input("Opción: ")
            print("")
            if(ans.upper() == "0"):
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print("Opción no valida, escoja una opción valida")
                time.sleep(2)
        return ans

    def limpiarPantalla(self):
        def clear():
            return os.system('clear')
        clear()

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, idusers):
        super().__init__(nombre, apellido, dni)
        self.idusers = idusers

    def toDic(self):
        d = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Dni": self.dni,
            "ID": self.idusers
        }
        return d

class Asistencia:
    def __init__(self, idUsuario, Dia, Entrada,Salida):
        self.idUsuario = idUsuario
        self.Dia = Dia
        self.Entrada = Entrada
        self.Salida = Salida

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
        #print(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                #print("removiendo archivo")
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
