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
    def __init__(self, nombre, apellido, sexo, dni):
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.dni=dni


class Usuario(Persona):
    def __init__(self, nombre, apellido, sexo, dni, codUsuario=0):
        super().__init__(nombre, apellido, sexo, dni)
        if codUsuario ==0:
            self.codUsuario = self.codUsuario +1
        else:
            self.codUsuario=codUsuario
    def __str__(self) -> str:
        return self.nombre+" ---- "+str(self.codUsuario)
    def toDic(self):
        d ={
            "nombre":self.nombre,
            "apellido":self.apellido,
            "sexo":self.sexo,
            "dni":self.dni,
            "codUsuario":self.codUsuario
        }
        return d

class Asistencia:
    def __init__(self,diaMarcado, horaEntrada, horaSalida, codUsuario):
        self.diaMarcado = diaMarcado
        self.horaEntrada=horaEntrada
        self.horaSalida=horaSalida
        self.cod=codUsuario
    def toDicA(self):
        d = {
            "dia":self.diaMarcado,
            "hora-entrada":self.horaEntrada,
            "hora-salida":self.horaSalida,
            "codigo":self.cod
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
                a=False
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b=b+1
                # exit()
            if (b>0):
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


#!==========================================================



#? VIENE LA CLASES DE ARCHIVO

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

