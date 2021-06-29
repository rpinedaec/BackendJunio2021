import os
import time
import json

from paquete.funciones import *
from paquete.clases import *



showHome = True
showUsuarios = True
showAsistencia = True

Home_op = {"Usuarios": "1", "Asistencia": "2", "Reportes": "3","Exit": "0"}
Menu_usuarios = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3","Mostrar Usuarios": "4", "Exit": "0"}
Menu_asistencia = {"Marcar Asistencia":"1","Exit":"0"}


listarUsuarios = []
listarUsuariosDIC =[]


# Asistencia
listarAsistencia = []
listarAsistenciaDic = []


fileUsuarios = Archivo("usuario.txt")
fileAsistencia =Archivo("asistencia.txt")

def cargainicial():
    res = fileUsuarios.leerArchivo()
    listTempUsuario = json.loads(res)
    for dic in listTempUsuario:
        newUser = Usuario(dic["nombre"],dic["apellido"],dic["sexo"],dic["dni"],dic["codUsuario"])
        listarUsuarios.append(newUser)
        listarUsuariosDIC.append(newUser.toDic())



def cargaAsistencia():
    res = fileAsistencia.leerArchivo()
    listTempAsistencia = json.loads(res)
    for dic in listTempAsistencia:
        newAsistencia = Asistencia(dic["dia"], dic["hora-entrada"], dic["hora-salida"], dic["codigo"])
        listarAsistencia.append(newAsistencia)
        listarAsistenciaDic.append(newAsistencia.toDicA())

cargaAsistencia()

cargainicial()

Main_menu = Menu("home", Home_op)
respuesta = Main_menu.show()

while showHome:
    if(respuesta == "0"):
        showHome=False
    elif(respuesta == "1"):
        while showUsuarios:
            menuUsuario = Menu("Usuario", Menu_usuarios)
            opUsuario = menuUsuario.show()
            if(opUsuario == "0"):
                exit()
            elif(opUsuario == "1"):
                nombre = input("Escribe tu nombre: ")
                apellido = input("Escribe tu apellido: ")
                sexo = input("Escribe tu sexo [ M - F ]: ")
                d = input("Escribe tu DNI: ")
                dni=validarDNI(d)
                cod = input("Escribe tu Codigo: ")
                codUsuario = validarCOD(cod)
                Users = Usuario(nombre, apellido, sexo, dni, codUsuario)
                listarUsuarios.append(Users)
                #?
                listarUsuariosDIC.append(Users.toDic())
                jsonString = json.dumps(listarUsuariosDIC)
                fileUsuarios.borrarArchivo()
                fileUsuarios.escribirArchivo(jsonString)
                print("Cliente Agregado")
                time.sleep(1)
            elif(opUsuario == '2'):
                cod= input("Ingrese el codigo para buscar: ")
                codUsuarioInput  = validarCOD(cod)
                for lista in listarUsuariosDIC:
                    if lista["codUsuario"] == codUsuarioInput:
                        print("Nombre: "+lista["nombre"] + "  Apellidos : "+lista["apellido"]+"  Sexo: "+lista["sexo"]+"  Dni: "+lista["dni"]+"  Codigo: "+lista["codUsuario"])
                        time.sleep(2)
                        break
                    else:
                        print("El usuario no se ha encontrado")
                        time.sleep(2)
                        break
            elif(opUsuario == '3'):
                cod= input("Ingrese el codigo para eliminar usuario: ")
                codUsuarioInput  = validarCOD(cod)
                #!
                for lista in listarUsuariosDIC:
                    if lista["codUsuario"] == codUsuarioInput:
                        usuarioEncontrado = lista
                        print("El usuario Nombre: "+lista["nombre"] + "  Apellidos : "+lista["apellido"]+" a sido eliminado")
                        listarUsuariosDIC.remove(lista)
                        jsonString = json.dumps(listarUsuariosDIC)
                        fileUsuarios.borrarArchivo()
                        fileUsuarios.escribirArchivo(jsonString)
                        time.sleep(3)
                        break
                    else:
                        print("El usuario no se ha encontrado")
                        time.sleep(2)
                        break
                    
            elif(opUsuario == '4'):
                print("Lista de usuarios")
                for lista in listarUsuariosDIC:
                    print("Nombre: "+lista["nombre"] + "  Apellidos : "+lista["apellido"]+"  Sexo: "+lista["sexo"]+"  Dni: "+lista["dni"]+"  Codigo: "+lista["codUsuario"])
                time.sleep(3)
    elif(respuesta =="2"):
        while showAsistencia:
                menuAsistencia = Menu("Asistencia",Menu_asistencia)
                opAsistencia = menuAsistencia.show()
                if(opAsistencia =="0"):
                    exit()
                elif(opAsistencia =="1"):
                    cod= input("Ingrese el codigo: ")
                    codUsuarioInput  = validarCOD(cod)
                    for lista in listarUsuariosDIC:
                        if lista["codUsuario"] == codUsuarioInput:
                            input("Presione Enter para marcar la Asistencia: ")
                            dia = dia()
                            horaE =horaES()
                            horaS = horaES()
                            asistencia =Asistencia(dia, horaE, horaS, codUsuarioInput)
                            listarAsistencia.append(asistencia)
                            #?
                            listarAsistenciaDic.append(asistencia.toDicA())
                            jsonString = json.dumps(listarAsistenciaDic)
                            fileAsistencia.borrarArchivo()
                            fileAsistencia.escribirArchivo(jsonString)
                            time.sleep(3)

    elif(respuesta == "3"):
        try:
            print("Mostrando usuarios que marcaron asistencia")
            cod= input("Ingrese el codigo: ")
            codUsuarioInput  = validarCOD(cod)
            for lista in listarUsuariosDIC:
                for li in listarAsistenciaDic:
                    if lista["codUsuario"] ==codUsuarioInput and li["codigo"] ==codUsuarioInput:
                        print("Nombre: "+lista["nombre"] + "  Apellidos : "+lista["apellido"]+"  Dni: "+lista["dni"]+"  Codigo: "+lista["codUsuario"]+" Dia: "+li["dia"]+" hora de entrada: "+li["hora-entrada"]+" hora de salida: "+li["hora-salida"])
            break
        except ValueError:
            print("Hubo un error")