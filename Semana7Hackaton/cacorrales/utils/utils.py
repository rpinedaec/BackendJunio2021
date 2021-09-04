import logging
import os
from time import sleep


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
    CEND = '\033[0m'
#-----------------
class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)

class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            self.limpiarPantalla()
            print(color.BLUE+"::::::::::::::::::BIENVENIDOS::::::::::::::::::"+color.CEND)
            print("")
            print(color.BLUE+":::::::::::::::::::" +self.name + "::::::::::::::::::"+color.CEND)
            print("")
            #print("")
            #print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
            #      self.name.upper()+"::::::::::::::::::::"+color.END)
            #print("")
            for (key, value) in self.op_list.items():
                print(key + color.GREEN + " :=→ " + color.CEND + value)
            print("")
            ans = input(
                color.YELLOW + "Por favor, ingrese su opción: " + color.CEND)
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
                print(color.RED + "Opción no valida, escoja una opción valida" + color.CEND)
                time.sleep(3)
        return ans

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()


#class Menu:
#    __log = log("Menu")
#    def __init__(self, nombreMenu, listaOpciones, pre_menu=0):
#        self.nombreMenu = nombreMenu
#        self.listaOpciones = listaOpciones
#        self.pre_menu = pre_menu
#
#    def mostrarMenu(self):
#        self.limpiarPantalla()
#        opSalir = True
#        while(opSalir):
#            self.limpiarPantalla()
#            print(color.BLUE+"::::::::::::::::::BIENVENIDOS::::::::::::::::::"+color.CEND)
#           print("")
#            print(color.BLUE+":::::::::::::::::::" +self.nombreMenu + "::::::::::::::::::"+color.CEND)
#            print("")
#            for (key, value) in self.listaOpciones.items():
#                print(key + color.GREEN + " : → " + color.CEND + value)
#            print("")
#            #for (key, value) in self.listaOpciones.items():
#            #    print(key, "\t:: ", value)
#            #opcion = 100
#            #print("\t- Salir \t\t::  9")
#            try:
#                print(color.CYAN+"Escoge tu opcion"+color.CEND)
#                opcion = int(input())
#            except ValueError as error:
#                self.__log.error(error)
#                print(color.RED+"Opcion invalida deben ser numeros del 0 al 4"+color.CEND)
#            contOpciones = 0
#            for (key, value) in self.listaOpciones.items():
#                if(opcion == int(value) or opcion == 9):
#                   contOpciones += 1
#            if(contOpciones == 0):
#                print(color.RED+"Escoge una opcion valida"+color.CEND)
#                self.__log.debug("No escoje opcion")
#                sleep(2)
#            else:
#                opSalir = False

#        return opcion

#   def limpiarPantalla(self):
#        def clear():
#            #return os.system('cls')
#            return os.system('clear')
#        clear()


class fileManager:
    logD = log("fileManager")

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
        self.logD.debug(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                self.logD.debug("removiendo archivo")

            except Exception as error:
                self.logD.error(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            self.logD.debug(path)
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    self.logD.error(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            self.logD.error(error)