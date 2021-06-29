from hackaton.hackaton import Ejercicio1 as test

try:
    lista = []
    serie = [3, 2, 7, 6, 5, 4, 3, 2]
    numeric = [6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5]
    alfabet = ["K", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    nombre = input("\033[1;32m"+"Ingrese su nombre: "+"\033[0;m")
    dni = input("\033[1;32m"+"Ingrese el número de DNI: "+"\033[0;m")
    long = len(dni)

    if (dni.isdigit() and long == 8): #Validación numérica y longitud.
        lista = list(dni)
        for i in range(len(lista)): #Convertir los datos de la lista a carácteres numéricos para facilitar el producto.
            lista[i] = int(lista[i])
        product = [x*y for x, y in zip(lista, serie)] #Multiplicar la lista con la serie.
        suma = sum(product) #Sumamos todos los productos.
        rest = suma % 11 #Obtener el residuo.

        if (rest != 0): #Si el residuo es diferente de 0, el valor 11 (por defecto) se le resta el residuo y se suma +1.
            i = (11 - rest) #No hay necesidad de sumar +1 ya que en lenguaje código [i] empieza de 0.
            verificador1 = numeric[i]
            verificador2 = alfabet[i]
        else: #Si la division es exacta que no tiene residuo la posición es 0.
            i = 0 #Recordar que i es la posición de la serie numérica y alfabética
            verificador1 = numeric[i]
            verificador2 = alfabet[i]  

        print(f"\x1b[1;31mPROCESANDO...\033[0;m")
        print(f"DNI válido: {dni}")
        print(f"Verificador numeric: {verificador1}")
        print(f"Verificador alfabet: {verificador2}")
        print(f"\x1b[1;33mHOLA {nombre} SU DNI ES {dni}-{verificador1} o {dni}-{verificador2}\033[0;m")

    else:
        print(
            f"\x1b[1;31mDNI no válido porque tiene {long} carácteres. Por favor, ingrese un dato numérico de 8 dígitos.\033[0;m")

except Exception as error:
    print("Lo sentimos hubo un error: ", error)