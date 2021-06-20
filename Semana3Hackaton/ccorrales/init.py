print ("****--VALIDAR SU NUMERO DE DNI--****")

nom = input("Ingrese su Nombre :")
ape = input("Ingrese su Apellido :")
num = (3,2,7,6,5,4,3,2)
#Descomponiendo el numero de DNI
lst = []
def string_int(my_data):
    for i in my_data:
        lst.append(int(i))    
    #print(lst)
while True:
    try:  
        dni = input("Ingrese el numero de DNI a validar  :")
        string_int(dni)
        break
    except ValueError:
        print ("No es un numero valido")
usuario = print ("Estimado  " + nom +"  "+ ape + "  su DNI es   :", lst)
dnivalor = lst
dni1=lst(0)*num(0)
print("dni1")
