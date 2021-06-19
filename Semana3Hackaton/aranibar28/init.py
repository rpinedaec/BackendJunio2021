from hackaton.hackaton import Ejercicio1 as test

try:
    dni = []
    control = True
    while control:
        resultado = input("Escribe el Nombre del USUARIO: ")
        dni.append(resultado)
except Exception as error:
    print("Hubo un error: ", error)

print(resultado)