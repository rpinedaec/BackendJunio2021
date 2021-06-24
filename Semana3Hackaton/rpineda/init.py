
tuplaMultiplicacion = (3,2,7,6,5,4,3,2)
dni= "47278876"
lisDNI = list(dni)
suma = 0
for indice in range(0,8,1):
    suma = suma + tuplaMultiplicacion[indice]* int(lisDNI[indice])

print(suma) 

# cod_val = input("Ingrese código validador de su DNI: ")
# diccionario = {1:6,2:7,3:8,4:9,5:0,6:1,7:1,8:2,9:3,10:4,11:5}
# while True:
#     if validar_entero(cod_val) and validar_longitud_cod(cod_val):
#         for clave in diccionario(0,10,1):
# 	        if cod_val == clave:
# 		        print(diccionario[clave])
#     else:  
#         print("Valor no válido, por favor vuelva a intentar")
#         cod_val = input("Ingrese código validador de su DNI: ")


diccionario = {1:6,2:7,3:8,4:9,5:0,6:1,7:1,8:2,9:3,10:4,11:5}
for key in diccionario:
     print(key, '->', diccionario[key])