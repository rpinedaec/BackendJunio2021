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

class Persona:
    def __init__(self, nombre, sexo, dni):
        self.nombre = nombre
        self.sexo = sexo
        self.dni = dni

class Cliente(Persona):
    def __init__(self, nombre, sexo, dni, codCliente=0):
        super().__init__(nombre, sexo, dni)
        if codCliente == 0:
            self.codCliente = self.codCliente + 1
        else:
            self.codCliente = codCliente

    def __str__(self) -> str:
        return self.nombre + " ---- " + str(self.codCliente)

    def comprar(self):
        print("Comprando")

        print("Termino de Comprar")


class Vendedor(Persona):
    def __init__(self, nombre, sexo, dni, codVendedor):
        super().__init__(nombre, sexo, dni)
        self.codVendedor = codVendedor

    def vender(self):
        print("Vendiendo")

        print("Termino de vender")


class Producto:

    def __init__(self, nombre, presentacion, precio):
        self.nombre = nombre
        self.presentacion = presentacion
        self.precio = precio

    def comprar(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad + cantidad
        print("termino de comprar")

    def vender(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad - cantidad
        print("termino de comprar")


class Helado(Producto):
    def __init__(self, nombre, presentacion, precio, sabor, tamaño, tipo):
        super().__init__(nombre, presentacion, precio) 
        self.sabor = sabor
        self.tamaño = tamaño
        self.tipo = tipo

    def preparar(self, cantidad):
        print("Se esta preparando el Helado")

class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo 

    def mostrarArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
            for linea in file.readlines():
                print(linea)
        except Exception as ex:
            print(ex)
        finally:
            file.close()

    def agregarPersona(self, persona):
        try:
            file = open(self.nombreArchivo, 'a')
            textoAgregar = "{},{},{} \n".format(persona.nombre, persona.sexo, persona.dni)
            file.write(textoAgregar)
        except Exception as ex:
            print(ex)
        finally:
            file.close()
            print(file)

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
                #return os.system('cls')
            return os.system('clear')
        clear()

Home_op = {"Clientes": "1", "Empleados": "2", "Exit": "0"}
Main_menu = Menu("home", Home_op)
respuesta = Main_menu.show()
print(respuesta)