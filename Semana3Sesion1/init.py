#Tipos de Ddatos Python
#String
mi_primera_variable = "Chao"
strMiSegundaVariable = "Hola"
strFrase = """Hola como estas
estoy bien 
que tal tu"""
strConcatenacion= mi_primera_variable + " "+strMiSegundaVariable
print (strMiSegundaVariable[1:3])
#Int
intMiPrimerEntero = -1
floatMiPrimerFloat = 3.14
comMiPrimerCcomplejo = 44j

intValor1 = 100
intValor2 = 200

print("La suma es igual a : " + str(intValor1 + intValor2))
print(f"La suma de {intValor1} + {intValor2} es {intValor1+intValor2}")
print("La resta es igual a : " + str(intValor1 - intValor2))
print("El producto es igual a : " + str(intValor1 * intValor2))
print("La división es igual a : " + str(intValor2 / intValor1))
print("La división entera es igual a : " + str(intValor2 // intValor1)) #División con resultado entero
print("El módulo es igual a : " + str(intValor2 % intValor1))

intValor1 = 21
intValor2 = 20

print(intValor1 % 2)
print(intValor2 % 2)

resp = intValor1 > intValor2
print(resp)

#Boolean
boolVal1 = intValor1 > intValor2
boolVal2 = False

print(boolVal1)

resp = boolVal1 and not boolVal2
print(resp)

(5*3+6)

#Tuplas
Tup = (1,2,3,4,5) #No cambia
TupDos = ("hola", 23, True, 22.4)

print(TupDos[3])
#List
Lst = [1,2,3,4,5]
print (Lst[2])
Lst.append("Ultimo")
print(Lst)

#Dictionary