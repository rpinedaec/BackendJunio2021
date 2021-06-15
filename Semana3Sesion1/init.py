# Tipos de Datos Python
# String
from typing import List


mi_primera_variable = "Chao"
strMiSegundaVariable = "Hola"
strFrase = """Hola como estas 
estoy bien
que tal tu"""
strConcatenacion = mi_primera_variable + " " + strMiSegundaVariable
print(strMiSegundaVariable[1:3])
# Int
intPrimerEnter = -1
floatMiPromerFloat = 3.14
comMiPrimerComplejo = 44j

intValor1 = 100
intValor2 = 200

print("la suma es igual a " + str(intValor1 + intValor2))
print(f"la suma de {intValor1} y {intValor2} es {(intValor1+intValor2)}")
print("Concatenando %f" % (5 * 8 + 0.1))
print(intValor1 - intValor2)
print(intValor1 * intValor2)
print(intValor2 / intValor1)
print(intValor2 // intValor1)
print(intValor2 % intValor1)

intValor1 = 21
intValor2 = 20

print(intValor1 % 2)
print(intValor2 % 2)

resp = intValor1 < intValor2
print(resp)
# Boolean
boolVal1 = intValor1 > intValor2
boolVal2 = False

print(not boolVal1)

resp = boolVal1 or boolVal2
print(resp)

print((5 * 3 + 4) + (6 * 2 + 5))
print(19 + 17)

# Tuplas
Tup = (1, 2, 3, 4, 5)
TupDos = ("hola", 23, True, 23, 23, 23)
print(TupDos.index("hola"))
"""print(str(TupDos.count(23)))
#List
Lst = ["hola", 23, True, 22.4]
print(Lst[1:3])
Lst.append("Ultimo")
Lst.remove(23)
Lst.remove(True)
Lst.pop()"""

# print(Lst.index("hola"))
# print(len(Lst))
tupla = tuple(range(1, 100))
print(tupla)


# Dictionary
dicDatos = {
    "Nombre": "Roberto",
    "Apellido": "Pineda",
    "Cursos": [1, 2, 3, 4, 5],
    "Titulos": {"UE": "UCE", "Titulo": "Ingeniero en Contabilidad y Auditoria"},
}

print(dicDatos.get("Titulos"))

sexo = ("Masculino", "Femenino")
genero = ["Hombre", "Mujer"]

# SETS

mySet = {"Uno", "Dos", 5, 4, 4, 2}
mySet.add(11)

print(mySet)

print(type(mySet))
print(type(sexo))
print(type(genero))
print(type(dicDatos))
