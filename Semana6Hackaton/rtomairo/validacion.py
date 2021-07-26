def validarDNI(arg):
    estado=True
    while estado:
        try:
            if(arg.isdigit() and len(arg)==8):
                estado=False
            else:
                arg = input("Error!, ingrese el N° dni completo: ")
        except ValueError as error:
            print(error)
    return arg


def validarNum(arg):
    estado=True
    while estado:
        try:
            if(arg.isdigit()):
                estado=False
            else:
                arg = input("Error!, no se admiten letras ingrese N°: ")
        except ValueError as error:
            print(error)
    return arg