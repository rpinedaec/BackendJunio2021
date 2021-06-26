from io import BufferedWriter


class Persona:
    def __init__(self, nombre, sexo, dni):
        self.nombre = nombre
        self.sexo = sexo
        self.dni = dni


class Cliente(Persona):
    def __init__(self, nombre, sexo, dni, codCliente=0):
        super().__init__(nombre, sexo, dni)
        if codCliente == 0:
            self.codCliente = self.codCliente + 1
        else:
            self.codCliente = codCliente

    def __str__(self) -> str:
        return self.nombre + " ---- " + str(self.codCliente)

    def comprar(self):
        print("Comprando")

        print("Termino de Comprar")


class Vendedor(Persona):
    def __init__(self, nombre, sexo, dni, codVendedor):
        super().__init__(nombre, sexo, dni)
        self.codVendedor = codVendedor

    def vender(self):
        print("Vendiendo")

        print("Termino de vender")


class Producto:

    def __init__(self, nombre, presentacion, precio):
        self.nombre = nombre
        self.presentacion = presentacion
        self.precio = precio

    def comprar(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad + cantidad
        print("termino de comprar")

    def vender(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad - cantidad
        print("termino de comprar")


class Helado(Producto):
    def __init__(self, nombre, presentacion, precio, sabor, tamaño, tipo):
        super().__init__(nombre, presentacion, precio) 
        self.sabor = sabor
        self.tamaño = tamaño
        self.tipo = tipo

    def preparar(self, cantidad):
        print("Se esta preparando el Helado")

print("Sistema de Venta de Helados")
listaCliente = []
listaProductos = []
while True:
    opMenu = int(input("Presiona 1 si eres cliente o 2 si eres vendedor o 9 si quieres salir: "))
    if opMenu == 9:
        break
    elif opMenu == 1:
        opCliente = int(input("eres cliente nuevo presiona 1 o si eres cliente antogui digit tu codigo  o 9 si quieres salir: "))
        if opCliente == 9:
            break
        elif opCliente == 1:
            nombre = input("Escribe tu nombre: ")
            sexo = input("Escribe tu sexo [ M - F ]: ")
            dni = input("Escribe tu DNI: ")
            cliente = Cliente(nombre, sexo, dni, 3)
            listaCliente.append(cliente)
            print("Cliente Agregado")
        else:
            for lista in listaCliente:
                print(lista)
            codigoCliente = int(input("Escribe tu codigo: "))
            clienteEncontado = None
            for item in listaCliente:
                if(item.codCliente == codigoCliente):
                    clienteEncontado = item
                    break
            if clienteEncontado:
                opEncontrado = int(input("Deseas Comprar un Helado 1, deseas salir 9"))
                if opEncontrado == 9:
                    break
                else:
                    clienteEncontado.comprar()

    elif opMenu == 2:
        opMenuVendedor = int(input("Comprar helado 1, vender helado 2, ver inventario 3, salir 9: "))
        if(opMenuVendedor == 9):
            break
        elif(opMenuVendedor == 1):
            print("Compar Helado")
            nombre = input("Escribe el nombre: ")
            presentacion = input("Escribe la presentacion: ") 
            precio = input("Escribe el precio: ") 
            sabor = input("Escribe el sabor: ")
            tamaño = input("Escribe el Tamaño: ")
            tipo = input("Escribe el tipo [Crema - Hielo]")

            helado = Helado(nombre, presentacion, precio, sabor, tamaño, tipo)
            listaProductos.append(helado)
        elif(opMenuVendedor == 3):
            for item in listaProductos:
                print(item.nombre)


