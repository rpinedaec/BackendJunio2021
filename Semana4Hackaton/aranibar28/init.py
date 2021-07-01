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
    def __init__(self, nombrePersona, apellidoPersona, dni):
        self.nombrePersona = nombrePersona
        self.apellidoPersona = apellidoPersona
        self.dni = dni

    def __str__(self) -> str:
        return f"{self.nombrePersona}, {self.apellidoPersona} - {self.dni}"

    def toDic(self):
        d = {
            "nombre": self.nombrePersona,
            "apellido": self.apellidoPersona,
            "dni": self.dni,
        }
        return d


class Jornada:
    def __init__(self, fecha, horaEntrada, horaSalida):
        self.fecha = fecha
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida

    def __str__(self) -> str:
        return f"{self.fecha}, {self.horaEntrada}"


class Asistencia(Persona, Jornada):
    def __init__(self, nombrePersona, apellidoPersona, dni, fecha, horaEntrada, horaSalida):
        Persona.__init__(self, nombrePersona, apellidoPersona, dni)
        Jornada.__init__(self, fecha, horaEntrada, horaSalida)

    def MarcarAsistencia(self):
        print("\nMarcando...")

    def toDic(self):
        d = {
            "nombre": self.nombrePersona,
            "apellido": self.apellidoPersona,
            "dni": self.dni,
            "fecha": self.fecha,
            "horaEntrada": self.horaEntrada,
            "horaSalida": self.horaSalida
        }
        return d


class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo, 'r')
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


class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            #self.limpiarPantalla()
            print("")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENÚ " +
                  self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(value + color.GREEN + " → " + color.END + key)
            print("")
            ans = input(
                color.YELLOW + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                print(color.RED + "Hasta, pronto\n" + color.END)
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED +
                      "\nOpción no valida, escoja una opción valida" + color.END)
                time.sleep(3)
        return ans

    def limpiarPantalla(self):
        def clear():
            return os.system("clear")
        clear()


lstPersona = []
lstPersonaDic = []

lstAsistencia = []
lstAsistenciaDic = []

fileDatos = Archivo("datos.txt")
fileAsistencia = Archivo("asistencia.txt")


def cargainicial():
    res = fileDatos.leerArchivo()
    listPersona = json.loads(res)
    for dic in listPersona:
        newPersona = Persona(
            dic["nombre"], dic["apellido"], dic["dni"])
        lstPersona.append(newPersona)
        lstPersonaDic.append(newPersona.toDic())


def cargaSecundaria():
    res = fileAsistencia.leerArchivo()
    lstMarcar = json.loads(res)
    for dic in lstMarcar:
        newAsistencia = Asistencia(
            dic["nombre"], dic["apellido"], dic["dni"], dic["fecha"], dic["horaEntrada"], dic["horaSalida"])
        lstAsistencia.append(newAsistencia)
        lstAsistenciaDic.append(newAsistencia.toDic())


showHome = True

opMenuPrincipal = {"Menú Usuario": "1", "Menú Asistencia": "2", "Salir": "0"}
ansMenuPrincipal = ""
menuPrincipal = Menu("Principal", opMenuPrincipal)

opMenuUsuario = {"Crear Usuario": "1", "Buscar Usuario": "2", "Eliminar Usuario": "3",
                 "Listar Usuario": "4", "Modificar Usuario": "5", "Salir": "0"}
ansMenuUsuario = ""
menuUsuario = Menu("Usuario", opMenuUsuario)

opMenuAsistencia = {"Marcar Asistencia": "1",
                    "Reporte por Usuarios": "2", "Reporte por Fechas": "3", "Salir": "0"}
ansMenuAsistencia = ""
menuAsistencia = Menu("Asistencia", opMenuAsistencia)

while showHome:
    ansMenuPrincipal = menuPrincipal.show()
    if(ansMenuPrincipal == "0"):
        break
    elif(ansMenuPrincipal == "1"):
        cargainicial()
        while showHome:
            ansMenuUsuario = menuUsuario.show()
            if(ansMenuUsuario == "0"):
                break
            elif(ansMenuUsuario == "1"):
                print(color.GREEN+"Crear Usuario"+color.END)
                nombre = input("Escribe nombre: ")
                apellido = input("Escribe apellido: ")
                dni = input("Escribe dni: ")
                usuario = Persona(nombre, apellido, dni)
                lstPersona.append(usuario)
                lstPersonaDic.append(usuario.toDic())
                jsonString = json.dumps(lstPersonaDic)
                fileDatos.borrarArchivo()
                fileDatos.escribirArchivo(jsonString)

            elif(ansMenuUsuario == "2"):
                dniPersona = input(
                    color.YELLOW+"Escribe DNI del Usuario a BUSCAR: "+color.END)
                vendMod = None
                encontro = False
                for item in lstPersona:
                    if(item.dni == dniPersona):
                        vendMod = item
                        encontro = True
                        break
                if(encontro):
                    print(color.GREEN + f"\nUsuario Encontrado: {item.__str__()}"+color.END)
                else:
                    print("El usuario no existe en la Base de Datos")

            elif(ansMenuUsuario == "3"):
                for item in lstPersona:
                    print(f"{item.__str__()}")
                dniPersona = input(
                    color.YELLOW+"\nEscribe DNI del Usuario a ELIMINAR: "+color.END)
                vendMod = None
                encontro = False
                for item in lstPersona:
                    if(item.dni == dniPersona):
                        vendMod = item
                        encontro = True
                        break
                if(encontro):
                    usuario = Persona(str(item.nombrePersona), str(item.apellidoPersona), str(item.dni))
                    lstPersona.remove(vendMod)
                    lstPersonaDic.remove(vendMod.toDic())
                    jsonString = json.dumps(lstPersonaDic)
                    fileDatos.borrarArchivo()
                    fileDatos.escribirArchivo(jsonString)
                print(color.RED+"Usuario Eliminado"+color.END)

            elif(ansMenuUsuario == "4"):
                print("Lista de Usuarios: ")
                for item in lstPersona:
                    print(f"{item.__str__()}")

            elif(ansMenuUsuario == "5"):
                for item in lstPersona:
                    print(f"{item.nombrePersona}, {item.apellidoPersona} DNI: {item.dni}")
                dniPersona = input(
                    color.YELLOW+"\nEscribe DNI del Usuario a modificar: "+color.END)
                vendMod = None
                encontro = False
                for item in lstPersona:
                    if(item.dni == dniPersona):
                        vendMod = item
                        encontro = True
                        break
                if(encontro):
                    nombre = input("Escribe nuevo nombre: ")
                    apellido = input("Escribe nuevo apellido: ")
                    dni = input("Escribe nuevo dni: ")
                    usuario = Persona(nombre, apellido, dni)
                    lstPersona.remove(vendMod)
                    lstPersona.append(usuario)
                    lstPersonaDic.remove(vendMod.toDic())
                    lstPersonaDic.append(usuario.toDic())
                    jsonString = json.dumps(lstPersonaDic)
                    fileDatos.borrarArchivo()
                    fileDatos.escribirArchivo(jsonString)
                print(color.GREEN+"\nUsuario Modificado"+color.END)

    elif(ansMenuPrincipal == "2"):
        cargaSecundaria()
        while showHome:
            ansMenuAsistencia = menuAsistencia.show()
            if(ansMenuAsistencia == "0"):
                break
            elif(ansMenuAsistencia == "1"):
                for item in lstPersona:
                    print(f"{item.nombrePersona}, {item.apellidoPersona} DNI: {item.dni}")
                dniPersona = input(
                    color.YELLOW+"\nDígite el DNI del usuario a Marcar Asistencia: "+color.END)
                vendMod = None
                encontro = False
                for item in lstPersona:
                    if(item.dni == dniPersona):
                        vendMod = item
                        encontro = True
                        break
                if(encontro):
                    print("\nMARCANDO ENTRADA DE "+str(item.nombrePersona))
                    nombre = str(item.nombrePersona)
                    apellido = str(item.apellidoPersona)
                    dni = str(item.dni)
                    fecha = input("Fecha: ")
                    horaEntrada = input("Hora de Entrada: ")
                    horaSalida = input("Hora de Salida: ")
                    usuario = Asistencia(
                        nombre, apellido, dni, fecha, horaEntrada, horaSalida)
                    lstAsistencia.append(usuario)
                    lstAsistenciaDic.append(usuario.toDic())
                    jsonString = json.dumps(lstAsistenciaDic)
                    fileAsistencia.borrarArchivo()
                    fileAsistencia.escribirArchivo(jsonString)
                print(color.GREEN+"\nEntrada asignada"+color.END)

            elif(ansMenuAsistencia == "2"):
                print("Lista de Asistencias por Usuarios")
                for item in lstAsistencia:
                    print(f"{item.nombrePersona}, {item.apellidoPersona} - {item.dni} || Fecha: {item.fecha} || Entrada: {item.horaEntrada} || Salida: {item.horaSalida}")

            elif(ansMenuAsistencia == "3"):
                print("Lista de Asistencias por Fechas")
                for item in lstAsistencia:
                    print(f"Fecha: {item.fecha} || Entrada: {item.horaEntrada} || Salida: {item.horaSalida}")
