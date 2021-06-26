from Validar.Validacion import *

control = True
dni = '0'
digito = '0'
while control:
	try:
		print("------------------------------------------------------------------")
		print("	Menú de opciones")
		pedirDatos = int(input("* Si desea ingresar el DNI precione == 1"
								+ "\n* Si desea ingresar el digito verificador precione == 2"
								+ "\n* Si desea validar el DNI precione == 3"
								+ "\n* Si desea mostrar los datos precione == 4"
								+ "\n* Si desea salir precione 0 \nIngrese: "))
		if(pedirDatos ==1):
			dni = input("Ingrese el N° de DNI: ")
			ValidarLongitudDNI(dni)
		elif(pedirDatos ==2):
			digito = input("Ingrese el digito verificador: ")
			validarLongitudVerficador(digito)
		elif(pedirDatos ==3):

			procesarValidacion(dni,digito)
		elif(pedirDatos ==4):
			mostrarDatos(dni,digito)
		elif pedirDatos==0:
			print("Vamos a salir")
			control = False
	except ValueError:
		print("Ingrese una opción valida")
		control = True