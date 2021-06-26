
from typing import Type



def Ejercicio1(objeto):    
    return type(objeto)


def Ejercicio2():
    a = 10
    b = -5
    c = "Hola"
    d = [1,2,3]
    print(a*5)
    print(a-b)
    print(c + "Mundo")
    print(c * 2)
    print(d[-1])
    print(d[1:])
    print(d+d)
    
def Ejercicio3():
    numero_1 = 9
    numero_2 = 3
    numero_3 = 6
    media = (numero_1 + numero_2 + numero_3) / 3
    print("La nota media es", media)
    return media

def Ejercicio4(num1,num2,num3):
    pond1 = num1 * 0.15
    pond2 = num2 * 0.35
    pond3 = num3 * 0.50
    result = round((pond1+pond2+pond3),2)
    return result

def Ejercicio5(matriz):
    print(matriz)
    matriz[0][-1]= sum(matriz[0]) - matriz[0][-1]
    matriz[1][-1]= sum(matriz[1]) - matriz[1][-1]
    matriz[2][-1]= sum(matriz[2]) - matriz[2][-1]
    matriz[3][-1]= sum(matriz[3]) - matriz[3][-1]
    print(matriz)
    
def Ejercicio6(lista):
    return "Hola"    
    
    