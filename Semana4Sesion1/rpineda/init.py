# CLASE Pinturas

class Pintura:
    __idPintura = 123
    __codigoRAF = "F22345"

    def __init__(self, color, volumen, tipo, marca):
        self.gama = color
        self.volumen = volumen
        self.tipo = tipo
        self.marca = marca

    def getId(self):
        return self.__idPintura

    def setId(self, nuevoID):
        self.__idPintura = nuevoID
  
    @property
    def codRAF(self):
        return self.__codigoRAF

    @codRAF.setter
    def codRAF(self, nuevoCodigo):
        self.__codigoRAF = nuevoCodigo

    def pintar(self, nroHoras):
        self.volumen = self.volumen - (nroHoras * 0.5)

    def comprar(self):
        self.volumen = 7.5
    
    

class Persona:
    def __init__(self, nombre, dni, sexo, edad):
        self.nombre = nombre
        self.dni = dni
        self.sexo = sexo
        self.edad = edad


class Cliente(Persona):
    def __init__(self, nombre, dni, sexo, edad, codCliente):
        super().__init__(nombre, dni, sexo, edad)
        self.codCliente = codCliente


class Empleado(Persona):
    def __init__(self, nombre, dni, sexo, edad, codPlanilla):
        super().__init__(nombre, dni, sexo, edad)
        self.codPlanilla = codPlanilla




# pintura1 = Pintura("Negro",  7.5, "Acrilico", "Vallejo")

# print(pintura1.marca)
# print(pintura1.tipo)
# print(pintura1.gama)

# pintura1.gama = "Negro OTAN"
# print(pintura1.gama)


# pintura2 = Pintura("Verde", 7.5, "Acrilico", "AMMO")

# print(pintura2.getId())

# print(pintura2.setId(456))

# print(pintura2.getId())

# print(pintura1.codRAF)
# pintura1.codRAF = "F445566"
# print(pintura1.codRAF)

per1 = Cliente("Roberto", "001575291", "Masculino", 37, 567)

per2 = Empleado("Karen", "999888", "Femenino", 26, 987)

print(per1.nombre)
print(per1.codCliente)

print(per2.nombre)
print(per2.codPlanilla)

pintura1 = Pintura("Negro",  7.5, "Acrilico", "Vallejo")
print(pintura1.volumen)
pintura1.pintar(3)
print(pintura1.volumen)
pintura1.pintar(5)
print(pintura1.volumen)

pintura1.pintar(10)
if(pintura1.volumen <= 0):
    print("Tienes que comprar uno nuevo")
    res = input("Quieres compara ahora escribe si o no? ")
    if(res == "si"):
        pintura1.comprar()

print(pintura1.volumen)