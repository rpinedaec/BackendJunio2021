#? validando la longitud del dni

def ValidarLongitudDNI(dni):
	estado = True
	while estado:
		try:
			dni = validarNumeroDni(dni)
			if(len(dni) !=8):
				dni = input("Ingrese el N° de DNI completo: ")				
			else:
				#!print("El Dni esta completo")
				estado=False
		except ValueError:
			print("El DNI esta incompleto")
	return dni

#? Validando el numero del dni
def validarNumeroDni(dni):
	estado = True
	while estado:
		try:
			if (type(int(dni))) == int:
				estado=False
		except ValueError:
				dni = input("Solo se admiten numeros, vuelva a Ingresar el DNI: ")

	return dni

def validarNumeroDigitoDni(dni):
	estado = True
	while estado:
		try:
			if (type(int(dni))) == int:
				estado=False
		except ValueError:
				dni = input("Solo se admiten numeros, vuelva a Ingresar el digito del DNI: ")

	return dni

#! Validando el digito del dni	

def validarLongitudVerficador(dni):
	estado = True
	while estado:
		try:
			dni = validarNumeroDigitoDni(dni)
			if(len(dni) !=1):				
				dni = input("Solo se admite un digito, vuelva a ingresar el digito del DNI: ")	
			else:
				#!print("Codigo verificador aceptado")
				estado=False
		except ValueError:
			print("Esta ingresando más de un digito")
	return dni

#! EValuando con diccionario
def procesarValidacion(dni,digitoDni):
	estado =True
	while estado:
		try:
			
			digitoVerficador = 0
			sumaDigitos = 0
			lst = []
			serieNumerica = (6,7,8,9,0,1,1,2,3,4,5)
			validador = (3,2,7,6,5,4,3,2)
			for d in range (len(validador)):
				#!print("El digito es: ",dni[d],"-",validador[d])
				lst.append(int(dni[d])*validador[d])
			sumaDigitos=sum(lst)
			cociente = sumaDigitos // 11		
			if sumaDigitos % 11==0:
				residuo = 0
			else:
				residuo = sumaDigitos %11
			digitoVerficador = 11 - residuo
			if int(digitoDni) !=serieNumerica[digitoVerficador]:
				print("El digito es incorrecto, vuelva a ingresar")
				break
			else:
				print("El DNI ES VALIDO")
				estado=False
		except IndexError:
			estado = False
			print("¡Ingrese valores !")

def mostrarDatos(dni,digitoDni):
	print(f"El N° DNI {dni} - {digitoDni}")
