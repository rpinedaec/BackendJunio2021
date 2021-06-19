def Ejercicio1(num1, num2):
    if num1 == num2:
        print("Son iguales")
    else:
        print("Son Diferentes")
 
    if num1 > num2:
        print("El primero es mayor que el segundo")
    else:
        if num2 >= num1:
            print("El segundo numero es mayor o igual que el primero")


def Ejercicio2(strCadena):
    nroCaracters = len(list(strCadena))
    if nroCaracters >= 3 and nroCaracters < 10:
        print(f"Pasword correcto cantidad de caractes: {nroCaracters}")
    else:
        print(f"Longitud del Passwords incorrecta: {nroCaracters}")

# def Ejercicio3(numero_usuario):
#     numero_magico = 12345679 
#     numero_usuario = numero_usuario * 9
