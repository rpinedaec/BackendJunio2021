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


print("Sistema de recarga de celulares")

class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    def __str__(self) -> str:
        return f"{self.nombre} -- {self.apellido}"
    
    def __repr__(self) -> str:
        return f"{self.nombre} -- {self.apellido}"
    
    def mostrar(self) -> str:
        return f"{self.nombre} -- {self.apellido}"

class Empresa:
    def __init__(self, nombreEmpresa, ruc):
        self.nombreEmpresa = nombreEmpresa
        self.ruc = ruc
    def mostrarRUC(self):
        return self.ruc

class Vendedor(Persona, Empresa):
    def __init__(self, nombrePersona, apellidoPersona, nombreEmpresa, dni, ruc):
        Persona.__init__(self, nombrePersona, apellidoPersona, dni)
        Empresa.__init__(self, nombreEmpresa, ruc)
    
    def VenderRecarga(self):
        print("Recargando...")
    
    def toDic(self):
        d = {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "empresa":self.nombreEmpresa,
            "dni":self.dni,
            "ruc":self.ruc
        }
        return d


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





lstVendedor = []
lstVendedorDic = []

fileVendedor = Archivo("vendedor.txt")

def cargainicial():
    res = fileVendedor.leerArchivo()
    print(res)
    listTempCliente = json.loads(res)
    for dic in listTempCliente:
        newCliente = Vendedor(dic["nombre"],dic["apellido"],dic["empresa"],dic["dni"],dic["ruc"])
        lstVendedor.append(newCliente)
        lstVendedorDic.append(newCliente.toDic())

cargainicial()
showHome = True
opMenuPrincipal ={"Crear Vendedor":"1", "Modificar Vendedor":"2", "Salir": "0"}
ansMenuPrincipal = "" 
menuPincipal = Menu("Menu Principal", opMenuPrincipal) 
while showHome:
    ansMenuPrincipal = menuPincipal.show()
    if(ansMenuPrincipal == "0"):
        break
    elif(ansMenuPrincipal == "1"):
        nombre = input("Escribe tu nombre: ")
        apellido= input("Escribe tu apellido: ")
        empresa= input("Escribe tu empresa: ")
        dni = input("Escribe tu dni: ")
        ruc= input("Escribe tu ruc: ")
        vendedor = Vendedor(nombre, apellido, empresa, dni, ruc)
        lstVendedor.append(vendedor)
        lstVendedorDic.append(vendedor.toDic())
        jsonString = json.dumps(lstVendedorDic)
        fileVendedor.borrarArchivo()
        fileVendedor.escribirArchivo(jsonString)

    elif(ansMenuPrincipal=="2"):
        for item in lstVendedor:
            print(f"{item.nombre} -- {item.apellido} -- {item.dni}")
        dniVendedor = input("Escribe tu DNI: ")
        vendMod = None
        encontro = False
        for item in lstVendedor:
            if(item.dni == dniVendedor):
                vendMod = item
                encontro = True
                break
        if(encontro):
            nombre = input("Escribe tu nombre: ")
            apellido= input("Escribe tu apellido: ")
            empresa= input("Escribe tu empresa: ")
            dni = input("Escribe tu dni: ")
            ruc= input("Escribe tu ruc: ")
            vendedor = Vendedor(nombre, apellido, empresa, dni, ruc)
            lstVendedor.remove(vendMod)
            lstVendedor.append(vendedor)
            lstVendedorDic.remove(vendMod.toDic())
            lstVendedorDic.append(vendedor.toDic())
            jsonString = json.dumps(lstVendedorDic)
            fileVendedor.borrarArchivo()
            fileVendedor.escribirArchivo(jsonString)

