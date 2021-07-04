###########################################
### HACKATON 04 - ASISTENCIAS EMPLEADO  ###
### Autor: Franklin Villafuerte Huincho ###
### Fecha: 28/06/2021                   ###
###########################################
import os   
import json
import time
from paquete.clases import *
from paquete.modulos import *


def cargaFileUsuario(lstCarga,archivo):
    res = archivo.leerArchivo()
    if os.stat("usuarios.txt").st_size > 0:
        lstTemp = json.loads(res)
        for dic in lstTemp:
            newUsers = Usuario(dic["Nombre"],dic["Apellido"],dic["Dni"],dic["ID"])
            ##listaCliente.append(newCliente)
            lstCarga.append(newUsers.toDic())

def cargaFileAsistencia(lstCarga,archivo):
    res = archivo.leerArchivo()
    if os.stat("asistencia.txt").st_size > 0:
        lstTemp = json.loads(res)
        for dic in lstTemp:
            newAsist = Asistencia(dic["ID"],dic["Dia"],dic["Entrada"],dic["Salida"])
            lstCarga.append(newAsist.toDic())


def updateFileUsers():
    jsonString = json.dumps(lisUsersDic)
    fileUsers.borrarArchivo()
    fileUsers.escribirArchivo(jsonString)

def updateFileAsist():
    jsonString = json.dumps(lisAsistDic)
    fileAsist.borrarArchivo()
    fileAsist.escribirArchivo(jsonString)

## Menu Usuarios
def mnuUsuarios():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Agregar Usuario":"1", "Buscar Usuario":"2", "Quitar Usuario":"3", "Listar Usuario":"4", "Salir": "0"}
    mnuSec = Menu("Gestionar Usuarios", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            AgregarUsuario()
            nombre = input("Nombre: ")
            apellido= input("Apellido: ")
            dni = pedirDNI()
            id = endIDUsuario(lisUsersDic)
            miUsuario = Usuario(nombre, apellido, dni, id)
            lisUsersDic.append(miUsuario.toDic())
            updateFileUsers()
            print("")
            input("Registro grabado correctamente, presione una tecla para continuar...")

        elif resMSec == "2":
            BuscarUsuario(lisUsersDic)

        elif resMSec == "3":
            opc = BorrarUsuario(lisUsersDic)
            if opc == "S":
                updateFileUsers()
                input("Registro eliminado correctamente, presione una tecla para continuar...")

        elif resMSec == "4":
            MostrarUsuario(lisUsersDic)
        elif resMSec == "0":
            bolSWmnu = False


# Menu Marcar Asistencia
def mnuMarcaAsis():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Marcar Entrada":"1", "Marcar Salida":"2", "Salir": "0"}
    mnuSec = Menu("Gestionar Asistencias", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            intID = MarcarID(lisUsersDic,"MARCAR ENTRADA")
            if intID > 0:
                print("Registro de Marcado")
                print("-------------------")
                print("Fecha: " + time.strftime("%x"))
                print("Hora " + time.strftime("%X"))
                bolFind = False
                for item in lisAsistDic:
                    if item['ID'] == intID and item['Dia'] == time.strftime("%x"):
                        bolFind = True
                        item['Entrada'] = time.strftime("%X")
                        updateFileAsist()
                        break
                
                if bolFind == False:
                    miMarcado = Asistencia(intID, time.strftime("%x"), time.strftime("%X"), "")
                    lisAsistDic.append(miMarcado.toDic())
                    updateFileAsist()
                print("")
                input("Se Registró la entrada correctamente, presione una tecla para continuar...")

        elif resMSec == "2":
            intID = MarcarID(lisUsersDic,"MARCAR  SALIDA")
            if intID > 0:
                print("Registro de Marcado")
                print("-------------------")
                print("Fecha: " + time.strftime("%x"))
                print("Hora " + time.strftime("%X"))
                bolFind = False
                for item in lisAsistDic:
                    if item['ID'] == intID and item['Dia'] == time.strftime("%x"):
                        bolFind = True
                        item['Salida'] = time.strftime("%X")
                        updateFileAsist()
                        break
                
                if bolFind == False:
                    miMarcado = Asistencia(intID, time.strftime("%x"), "", time.strftime("%X"))
                    lisAsistDic.append(miMarcado.toDic())
                    updateFileAsist()
                print("")
                input("Se Registró la salida correctamente, presione una tecla para continuar...")

        elif resMSec == "0":
            bolSWmnu = False

# Menu Reporte Asistencia
def mnuReportAsis():
    os.system('clear')
    resMSec = ""
    opMnuSec ={"Reporte por Usuario":"1", "Reporte por Día":"2", "Salir": "0"}
    mnuSec = Menu("Reporte de Asistencias", opMnuSec) 
    bolSWmnu = True
    while bolSWmnu:
        resMSec = mnuSec.show()
        if resMSec == "1":
            ListarAsistUsuario(lisUsersDic,lisAsistDic)

        elif resMSec == "2":
            ListarAsistFecha(lisUsersDic,lisAsistDic)

        elif resMSec == "0":
            bolSWmnu = False


####################
## Menu Principal ##
####################

fileUsers = Archivo("usuarios.txt")
fileAsist = Archivo("asistencia.txt")

lisUsersDic = []
lisAsistDic = []

respMenu = "" 
opMainMenu ={"Usuarios":"1", "Asistencias":"2", "Reportes":"3", "Salir": "0"}
menuPincipal = Menu("Menu Principal - Ctrl.Asistencia", opMainMenu) 
bolSW = True
while bolSW:
    respMenu = menuPincipal.show()
    if respMenu == "1":
        lisUsersDic = []
        cargaFileUsuario(lisUsersDic,fileUsers)
        mnuUsuarios()

    elif respMenu == "2":
        lisUsersDic = []
        cargaFileUsuario(lisUsersDic,fileUsers)
        lisAsistDic = []
        cargaFileAsistencia(lisAsistDic,fileAsist)
        mnuMarcaAsis()

    elif respMenu == "3":
        lisUsersDic = []
        cargaFileUsuario(lisUsersDic,fileUsers)
        lisAsistDic = []
        cargaFileAsistencia(lisAsistDic,fileAsist)        
        mnuReportAsis()

    elif respMenu == "0":
        bolSW = False
