from introduccion.introduccion import Ejercicio1 as eje1
from introduccion.introduccion import Ejercicio2 as eje2
from introduccion.introduccion import Ejercicio3 as eje3
from introduccion.introduccion import Ejercicio4 as eje4
from introduccion.introduccion import Ejercicio5 as eje5
from introduccion.introduccion import Ejercicio6 as eje6

print ("++++++++++ Ejercicio 1 ++++++++++")

var1 = "Hola Mundo"
print(eje1(var1))
var2 = (1,10,100)
print(eje1(var2))
var3 = -25
print(eje1(var3))
var4 = 1.167
print(eje1(var4))
var5 = ["Hola Mundo"]
print(eje1(var5))

print(" ")
print("++++++++++ Ejercicio 2 ++++++++++")
eje2()

print(" ")
print("++++++++++ Ejercicio 3 ++++++++++")
eje3()

print(" ")
print("++++++++++ Ejercicio 4 ++++++++++")
print(eje4(10,7,4))

print(" ")
print("++++++++++ Ejercicio 5 ++++++++++")
matriz =[
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13],
]
print(eje5(matriz))

print(" ")
print("++++++++++ Ejercicio 6 ++++++++++")
lista=["Karen", "Lam", 20]
print(eje6(lista))
