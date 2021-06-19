from hackaton.hackaton import Ejercicio1 as test

try:
    lista = []
    serie = [3, 2, 7, 6, 5, 4, 3, 2]
    numeric = [6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5]
    alfabet = ["K", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    nombre = input("\033[4;32m"+"Ingrese su nombre: "+"\033[0;m")
    dni = input("\033[4;32m"+"Ingrese el número de DNI: "+"\033[0;m")
    long = len(dni)

    if (dni.isdigit() and long == 8):
        lista = list(dni)
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        product = [x*y for x, y in zip(lista, serie)]
        suma = sum(product)
        rest = suma % 11
        if (rest == 0):
            i = 0
            verificador1 = numeric[i]
            verificador2 = alfabet[i]
        else:
            i = (11 - rest) + 1
            verificador1 = numeric[i-1]
            verificador2 = alfabet[i]
        print(f"\x1b[1;31mPROCESANDO...\033[0;m")
        print(f"DNI válido: {dni}")
        print(f"Verificador numeric: {verificador1}")
        print(f"Verificador alfabet: {verificador2}")
        print(f"\x1b[1;33mHOLA {nombre} SU DNI ES {dni}-{verificador1} o {dni}-{verificador2}\033[0;m")

    else:
        print(
            f"DNI no válido porque tiene {long} carácteres. Ingrese un dato numérico porfavor.")

except Exception as error:
    print("Lo sentimos hubo un error: ", error)
