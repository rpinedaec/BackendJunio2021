# ----- Ejercicio DIGITO VALIDADOR
from paquete.validaciones import *
lstDNI = []
intDV = 0
bolSW = True
while bolSW:
    print("MENU PRINCIPAL")
    print("==============")
    print("[1] Ingresar DNI")
    print("[2] Ingresar Dígito Validador")
    print("[3] Ver Datos Ingresados")
    print("[4] Verificar Dígito Validador")
    print("[0] Salir")
    intOpc = pedirNumeroEntero("Opción: ")
    if intOpc == 1:
        lstDNI = pedirDNI()
    elif intOpc == 2:
        intDV = pedirDV()
    elif intOpc == 3:
        verDatos(lstDNI,str(intDV))
    elif intOpc == 4:
        validarDV(lstDNI,str(intDV))
    elif intOpc == 0:
        bolSW = False
    else:
        print("Introduce un número entre 0-3")
