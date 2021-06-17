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

from operadores.operadores import Ejercicio1 as test
from operadores.operadores import Ejercicio2 as test2

# num1 = input("Ingresa el primer numero ")
# num2 = input("Ingresa el segundo numero ")

# test(num1, num2)

try:
    password = input("Ingresa tu password ")
    test2(password)
except Exception as error:
    print("hubo un error y es: ", error)
