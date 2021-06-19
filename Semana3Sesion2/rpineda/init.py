# from introduccion.introduccion import Ejercicio1 as eje1
# from introduccion.introduccion import Ejercicio2 as eje2
# from introduccion.introduccion import Ejercicio3 as eje3
# from introduccion.introduccion import Ejercicio4 as eje4
# from introduccion.introduccion import Ejercicio5 as eje5
# from introduccion.introduccion import Ejercicio6 as eje6

# print("Ejercicio 1")
# var1 = "Hola Mundo"
# print(eje1(var1))
# var2 = [1, 10, 100]
# print(eje1(var2))
# var3 = -25
# print(eje1(var3))
# var4 = 1.167
# print(eje1(var4))
# var5 = ("Hola", "Mundo")
# print(eje1(var5))
# print("Ejercicio 2")
# eje2()
# print("Ejercicio 3")
# eje3()
# print("Ejercicio 4")
# print(eje4(10, 7, 4))
# print("Ejercicio 5")
# lista = [
#     [1, 1, 1, 3],
#     [2, 2, 2, 7],
#     [3, 3, 3, 9],
#     [4, 4, 4, 13]
# ]
# print(eje5(lista))

# print("Ejercicio 6")
# lista = ["Karen", "Lam", 20]
# eje6(lista)

# from operadores.operadores import Ejercicio1 as test
# from operadores.operadores import Ejercicio2 as test2



# num1 = input("Ingresa el primer numero ")
# num2 = input("Ingresa el segundo numero ")

# test(num1, num2)

# try:
#     password = input("Ingresa tu password ")
#     test2(password)
# except Exception as error:
#     print("hubo un error y es: ", error)

# from colecciones.colecciones import Ejercicio1 as test

# try:
#     usuario = []
#     admins = []
#     control = True
#     while control:
#         pedirDatos = int(input("Si quieres agregar nombres a USUARIO marca 1 "
#                                 + "\nSi quieres agregar nombres a ADMINS marca 2 "
                                
#                                 + "\nSi quieres Borrar un USUARIO marca 3"
#                                 + "\nSi quieres Borrar un ADMINS marca 4"
#                                 + "\nSi quieres agregar 5 nombres a USUARIO marca 5 "
#                                 + "\nSi quieres SALIR marca 0  \n"))
#         if(pedirDatos == 1):
#             nombre = input("Escribe el Nombre del USUARIO: ")
#             usuario.append(nombre)
#         if(pedirDatos == 2):
#             nombre = input("Escribe el Nombre del ADMINS: ")
#             admins.append(nombre)
#         if(pedirDatos == 3):
#             print("Esta es la lista de USUARIOS")
#             for nombres in usuario:
#                 print(nombres)
#             nombre = input("Escribe el Nombre del USUARIO a Borrar: ")
#             usuario.remove(nombre)
#         if(pedirDatos == 4):
#             nombre = input("Escribe el Nombre del ADMINS a Borrar: ")
#             admins.remove(nombre)
#         if(pedirDatos == 5):
#             for i in range(1, 6, 1):
#                 nombre = input(f"Escribe el Nombre {i} del USUARIO: ")
#                 if(nombre == "David"):
#                     break
#                 usuario.append(nombre)
#         if(pedirDatos == 0):
#             print("salir")
#             control = False
#             #salir

# except ValueError as errorValor:
#     print("No puedes borrar un nombre que no este en la lista " + str(errorValor))

# except Exception as error:
#     print("hubo un error " + error)
# print(usuario)
# print(admins)

# print("Sistema de Prioridades de Proyectos")

# try:
#     tareas = []
#     control = True
#     while control:
#         pedirDatos = int(input("Si quieres agregar una tarea marca 1 "
#                                 + "\nSi quieres Borrar una tarea marca 2 "
#                                 + "\nSi quieres cambiar la prioridad marca 3"
#                                 + "\nSi quieres SALIR marca 0  \n"))
#         if(pedirDatos == 1):
#             nombre = input("Escribe el Nombre de la Tarea: ")
#             tareas.append(nombre)
#         if(pedirDatos == 2):
#             i = 1
#             for nombres in tareas:
#                 print(f"{i} --- {nombres}")
#                 i = i+1
#             nombre = input("Escribe el Nombre de la tarea a borrar: ")
#             tareas.remove(nombre)
#         if(pedirDatos == 3):
#             print("Esta es la lista de Tareas")
#             i = 0
#             for nombres in tareas:
#                 print(f"{i} --- {nombres}")
#                 i = i+1
#             nombre = input("Escribe en nombre de la tarea: ")
#             prioridad = int(input("Escribe la prioridad"))
#             tareas.remove(nombre)
#             tareas.insert(prioridad, nombre)
#             i = 1
#             for nombres in tareas:
#                 print(f"{i} --- {nombres}")
#                 i = i+1
#         if(pedirDatos == 0):
#             print("salir")
#             control = False
#             #salir

# except ValueError as errorValor:
#     print("No puedes borrar un nombre que no este en la lista " + str(errorValor))

def listToString(s):
    str1 = "" 
    return (str1.join(s))
        
        
# print(tareas)
print("Sistema de Alineacion de caracteres")
# ***********HolaMundo
linea = []
palabra = "HolaMundo"
lstPalabra = list(palabra[::-1])
for valor in range(0,20,1):
    try:
        linea.append(lstPalabra[valor])
    except Exception as error:
        linea.append("*")
print(linea)

print(listToString(linea)[::-1])


