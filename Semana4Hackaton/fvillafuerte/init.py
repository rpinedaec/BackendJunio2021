###########################################
### HACKATON 04 - ASISTENCIAS EMPLEADO  ###
### Autor: Franklin Villafuerte Huincho ###
### Fecha: 28/06/2021                   ###
###########################################
import os   
import json
from paquete.clases import *
from paquete.modulos import *


def cargaFileUsuario(lstCarga,archivo):
    res = archivo.leerArchivo()
    if os.stat("usuarios.txt").st_size > 0:
        lstTemp = json.loads(res)
        print(lstTemp)
        for dic in lstTemp:
            newUsers = Usuario(dic["Nombre"],dic["Apellido"],dic["Dni"],dic["ID"])
            ##listaCliente.append(newCliente)
            lstCarga.append(newUsers.toDic())

def updateFileUsers():
    jsonString = json.dumps(lisUsersDic)
    fileUsers.borrarArchivo()
    fileUsers.escribirArchivo(jsonString)


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


## Menu Principal
fileUsers = Archivo("usuarios.txt")
lisUsersDic = []
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
        os.system('clear')
        ans = input("Asistencia: ")
    elif respMenu == "3":
        os.system('clear')
        ans = input("reporte: ")
    elif respMenu == "0":
        bolSW = False
