 HACKATON SEMANA 3
# VALIDACIÓN DE DNI

#Funciones
def validar_entero(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def validar_longitud_dni(num):
    try:
        if len(num)== 8:
            return True
        else:
            return False
    except ValueError:
        return False 
    
def validar_longitud_cod(num):
    try:
        if len(num)== 1:
            return True
        else:
            return False
    except ValueError:
        return False 



#VERIFICANDO DNI
dni = input("Ingrese DNI: ")
while True:
    if validar_entero(dni) and validar_longitud_dni(dni):
        print("El valor ingresado es correcto") 
        break
    else:  
        print("Valor no válido, por favor vuelva a intentar")
        dni = input("Ingrese su número de DNI: ")
#CONVIRTIENDO DNI A LISTA 
producto_ind = 0
multip= (3,2,7,6,5,4,3,2)
lstDNI = list(dni)

#MULTIPICANDO LISTA x TUPLA
for indice in range(0,8,1):
    producto_ind += multip[indice]* int(lstDNI[indice])

#HALLANDO CÓDIGO VALIDADOR A PARTIR DEL DNI
mod = producto_ind % 11
rest= 11 - mod
sum_1 = rest + 1
print(sum_1)

#VERIFICANDO CODIGO DE VALIDACIÓN
cod_val = input("Ingrese código validador: ")
diccionario = {1:6,2:7,3:8,4:9,5:0,6:1,7:1,8:2,9:3,10:4,11:5}

while True:

    if validar_entero(cod_val) and validar_longitud_cod(cod_val):
        print("Código ingresado de manera correcta")
        break
    else:  
        print("Valor no válido, por favor vuelva a intentar")
        cod_val = input("Ingrese código validador de su DNI:  ")
       
#COMPARANDO CON LO INGRESADO POR EL USUARIO
for key in diccionario:
        if diccionario[key] == cod_val:
            print("El código validador ingresado es correcto")  
