class Persona:
    def __init__(self, nombre, dni, sexo, edad):
        self.nombre = nombre
        self.dni = dni
        self.sexo = sexo
        self.edad = edad

    def caminar(self):
        print("Esta caminando")
    
    def registar(self):
        print("me estoy registrando")
        return False
    
    def sumar(self, num1, num2=10):
        result = num1+num2
        return result

    def nombrar(self, nombrar):
        for item in nombrar:
            print(item)
    
    def dicNombrar(self, **dicLista):
        print(dicLista)
        print(dicLista['param1'])
        print(dicLista['param2'])


class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, edad, codCliente):
        super().__init__(nombre, dni, sexo, edad)
        self.codCliente = codCliente


class Empleado(Persona):
    def __init__(self, nombre, dni, sexo, edad, codEmpleado):
        super().__init__(nombre, dni, sexo, edad)
        self.codEmpleado = codEmpleado
    
    def marcarAsistencia(self, hora):
        print(f"Marco asistencia a las {hora}")
        return "Se marco correctamente"

class Plastimodelos:
    __Numero = 0
    __Modelo = ""

    def __init__(self):
        self.__Modelo = "HobbyColor"
        self.__Numero = 1

    def __del__(self):
        print("Borrando de Memoria")

    def __str__(self) -> str:
        return self.__Modelo

    @property
    def numero(self):
        return self.__Numero

    @numero.setter
    def numero(self, nuevoNumero):
        self.__Numero = nuevoNumero

        


empleado = Empleado("Karen", 123456, "Femenino", 26, 98765)

print(empleado.marcarAsistencia("19:30"))

empleado.caminar()

cliente = Cliente("Roberto", 9876, "M", 37, 646464)

if cliente.registar():
    print("se registro correctamente")
else:
    print("No se registro")

resultado = empleado.sumar(num2=33, num1=55)
print(resultado)

lis = ["33", "Roberto", 22]

empleado.nombrar(lis)
cliente.dicNombrar(param1="Hola", param2="chao")

avion = Plastimodelos()
print(avion.numero)
avion.numero = 33
print(avion.numero)

print(avion)

#del(avion)

#print(avion.numero)