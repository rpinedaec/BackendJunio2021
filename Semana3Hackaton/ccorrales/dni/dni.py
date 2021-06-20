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
        print ("No es un numero DNI valido")
usuario = print ("Estimado  " + nom +"  "+ ape + "  su DNI es   :", lst)

def valdni(lstVer,strDV):
    lst1 = [3,2,7,6,5,4,3,2]
    lst2 = [6,7,8,9,0,1,1,2,3,4,5]
    x = 0
    intRDV = 0
    for strDato in lstVer:
        intRDV = intRDV + (int(strDato) * lst1[x])
        x = x + 1
    intRDV = intRDV % 9
    intRDV = 11 - intRDV
    if intRDV == 11:
        intRDV = 0
    intRDV = intRDV + 1
    intRDV = lst2[intRDV - 1]
    if intRDV == int(strDV):
        print ("su numero validador es"+intRDV)
