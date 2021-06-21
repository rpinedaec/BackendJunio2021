def pedirNumeroEntero(strMsg):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(strMsg))
            correcto = True
        except ValueError:
            print('Error, Ingrese número entero')
    return num

def pedirDNI():
    correcto = False
    while(not correcto):
        num = pedirNumeroEntero("Ingrese N°DNI: ")
        if len(str(num)) == 8:
            correcto = True
        else:
            print("N° de dígitos incorrectos")
    return list(str(num))

def pedirDV():
    correcto = False
    while(not correcto):
        num = pedirNumeroEntero("Ingrese Dígito Validaror: ")
        if len(str(num)) == 1:
            correcto = True
        else:
            print("Dni tiene más de 1 dígito")
    return num 

def verDatos(lstVer,strDV):
    strCade = ""
    for strNom in lstVer:
        strCade = strCade + strNom
    print("N° DNI: " + strCade +" - " +strDV)

def validarDV(lstVer,strDV):
    lstVar1 = [3,2,7,6,5,4,3,2]
    lstVar2 = [6,7,8,9,0,1,1,2,3,4,5]
    x = 0
    intRDV = 0
    for strDato in lstVer:
        intRDV = intRDV + (int(strDato) * lstVar1[x])
        x = x + 1
    intRDV = intRDV % 9
    intRDV = 11 - intRDV
    if intRDV == 11:
        intRDV = 0
    intRDV = intRDV + 1
    intRDV = lstVar2[intRDV - 1]
    if intRDV == int(strDV):
        print("¡ Dígito Validador CORRECTO..!")
    else:
        print("¡ Dígito Validador INCORRECTO..!")
