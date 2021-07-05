def prueba():
    serie= [3,2,7,6,5,4,3,2]
    divisor = 11
    resultado = 0
    residuo = 0
    i=0
    digValid = ""
    serieNumerica = [6,7,8,9,0,1,1,2,3,4,5]
    seriaAlfabetica = ["K","A","B","C","D","E","F","G","H","I","J"]   
    dni = input("Introduzca únicamente los números de su DNI: ")
    digDni = list(map(int, str(dni)))
    if len(dni) != 8:
        print("Serie incorrecta")
    else:
        
    #Separa cada digito de dni que se ingresa
     print("la cantidad de digitos de dni es: "+str(len(dni)))
     print("La serie es: "+str(digDni))
      #Multiplicar cada digito con la serie y sumarlo
     for strDato in digDni:
        resultado = resultado + (int(strDato) * serie[i])
        i+=1
        print("La suma de todos los digitos es:"+str(resultado))
     #Divir el resultado entre 11 y se resta con el residuo
     residuo = resultado % divisor
     print("El residuo es: "+str(residuo))
     #el divisor se resta con el residuo, si el residuo es 0 el resultado es 0
     if residuo == 0:
         resultado = 0 
         print("El digito validador es 0")
     else: 
         resultado = divisor - residuo 
         #Al resultado le sumamos 1
         resultado = resultado+1
         print("La posicion del digito es: "+str(resultado))
         digValid = str(serieNumerica[resultado])+seriaAlfabetica[resultado]
         print("El digito validador es: "+digValid)
