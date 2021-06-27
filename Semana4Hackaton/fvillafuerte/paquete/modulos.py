import os
import json
from paquete.clases import *

def pedirNumeroEntero(strMsg):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(strMsg))
            correcto = True
        except ValueError:
            print('Error, Ingrese número entero')
    return num

def pedirDNI():
    correcto = False
    while(not correcto):
        num = pedirNumeroEntero("N° DNI: ")
        if len(str(num)) == 8:
            correcto = True
        else:
            print("N° de dígitos incorrectos")
    return str(num)

def valOpc():
    correcto = False
    while(not correcto):
        opc = input("Esta seguro de Elimar? [S]i, [N]o : ")
        opc = opc.upper()
        if opc == 'S' or opc == 'N' :
            correcto = True
        else:
            print("Opción no válida, ...")
    return opc

### FUNCION ALIENAR TEXTO
def alinear_texto(strTexto,intAncho,strCad,strOPC):
    intLong = len(strTexto)
    if intLong <= intAncho:
        if strOPC == "I":
            strC1 = ""
            strC2 = strCad * (intAncho - intLong)        
        if strOPC == "C":
            intPos = int((intAncho - intLong) / 2)
            strC1 = strCad * intPos
            strC2 = strCad * (intAncho - (intPos + intLong))
        if strOPC == "D":
            strC1 = strCad * (intAncho - intLong)
            strC2 = ""        
        strTexto = strC1 + strTexto + strC2
    else:
        raise ValueError("Nro. caracteres superior al ancho de alineación")
    return strTexto


def AgregarUsuario():
    os.system('clear')
    print("REGISTRO DE USUARIOS")
    print("====================")
    print("")

def endIDUsuario(lisUsersDic):
    intID = 0
    for key in lisUsersDic:
        if key['ID'] > intID:
            intID = key['ID']
    intID = intID + 1
    return intID

def BuscarUsuario(lisUsersDic):
    os.system('clear')
    print("BUSQUEDA DE USUARIOS")
    print("====================")
    print("")
    idBusca = pedirNumeroEntero("ID Usuario: ")
    bolFind = False
    for item in lisUsersDic:
        if item['ID'] == idBusca:
            bolFind = True
            print("DATOS DEL USUARIO")
            print("-----------------")
            print("ID : " + str(item['ID']) + ", Nombres: " + item['Nombre'] + " " + item['Apellido'] + ", DNI: " + item['Dni'])
            print("")
            input("presione una tecla para continuar...")
            break
    if bolFind == False:
        print("")
        input("ID NO EXISTE, presione una tecla para continuar...")

def BorrarUsuario(lisUsersDic):
    opc = "N"
    os.system('clear')
    print("ELIMINAR USUARIOS")
    print("=================")
    print("")
    idBusca = pedirNumeroEntero("ID Usuario: ")
    bolFind = False
    for item in lisUsersDic:
        if item['ID'] == idBusca:
            bolFind = True
            print("DATOS DEL USUARIO")
            print("-----------------")
            print("ID : " + str(item['ID']) + ", Nombres: " + item['Nombre'] + " " + item['Apellido'] + ", DNI: " + item['Dni'])
            print("")
            opc = valOpc()
            if opc == "S":
                lisUsersDic.remove(item)                        
            break
    if bolFind == False:
        print("")
        input("ID NO EXISTE, presione una tecla para continuar...")
    return opc

def MostrarUsuario(lisUsersDic):
    os.system('clear')
    print("REPORTE DE USUARIOS")
    print("====================")
    print("")
    for key in lisUsersDic:
        print("ID : " + str(key['ID']) + ", Nombres: " + key['Nombre'] + " " + key['Apellido'] + ", DNI: " + key['Dni'])
    print("")
    input("Presione una tecla para continuar....")

def MarcarID(lisUsersDic,strMSG):
    intID = 0
    os.system('clear')
    print(strMSG)
    print("==============")
    print("")
    idBusca = pedirNumeroEntero("Marcar Asistencia del Usuario(ID): ")
    bolFind = False
    for item in lisUsersDic:
        if item['ID'] == idBusca:
            bolFind = True
            print("Nombres: " + item['Nombre'] + " " + item['Apellido'])
            intID = item['ID']
            break
    if bolFind == False:
        print("")
        input("ID NO EXISTE, presione una tecla para continuar...")
    return intID

def ListarAsistUsuario(lisUsersDic,lisAsistDic):
    os.system('clear')
    print("REPORTE DE ASISTENCIA X USUARIO")
    print("===============================")
    idBusca = pedirNumeroEntero("ID Usuario: ")
    bolFind = False
    for item in lisUsersDic:
        if item['ID'] == idBusca:
            bolFind = True
            print("Nombres: " + item['Nombre'] + " " + item['Apellido'])
            print("")
            print("   DIA    ENTRADA    SALIDA")
            print("----------------------------")
            for key in lisAsistDic:
                if key['ID'] == idBusca:
                    print(key['Dia'] + "  " + key['Entrada'] + "  " + key['Salida'])

            print("")
            input("Presione una tecla para continuar....")
            break

    if bolFind == False:
        print("")
        input("ID NO EXISTE, presione una tecla para continuar...")

def ListarAsistFecha(lisUsersDic,lisAsistDic):
    os.system('clear')
    print("REPORTE DE ASISTENCIA X DIA")
    print("===============================")
    strBusca = input("Fecha (campo vacio-todos): ")
    strNom = ""
    print("")
    print("   DIA    ENTRADA    SALIDA")
    print("----------------------------")
    for key in lisAsistDic:
        if strBusca == "":
            idBusca = key['ID']
            for item in lisUsersDic:
                if item['ID'] == idBusca:
                    strNom = item['Nombre'] + " " + item['Apellido']
            print(key['Dia'] + "  " + key['Entrada'] + "  " + key['Salida'] + "  " + strNom)

        if strBusca != "":
            if key['Dia'] == strBusca:
                idBusca = key['ID']
                for item in lisUsersDic:
                    if item['ID'] == idBusca:
                        strNom = item['Nombre'] + " " + item['Apellido']
                print(key['Dia'] + "  " + key['Entrada'] + "  " + key['Salida'] + "  " + strNom)
    print("")
    input("Presione una tecla para continuar....")

