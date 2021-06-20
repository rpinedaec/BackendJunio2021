print ("****--VALIDAR SU NUMERO DE DNI--****")
nom = input("Ingrese su Nombre :")
ape = input("Ingrese su Apellido :")
lst = []
def string_int(my_data):
    for i in my_data:
        lst.append(int(i))    
    print(lst)
while True:
    try:  
        dni = input("Ingrese el numero de DNI a validar  :")
        string_int(dni)
        break
    except ValueError:
        print ("No es un numero DNI valido")
usuario = print ("Estimado  " + nom +"  "+ ape + "  su DNI es   :", lst)
def codval(x):
    for indice in range(0,8,1):
        print(indice)
        