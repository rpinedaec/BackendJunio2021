from conexion import conexion
import os
import time
from tabulate import tabulate

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Lector:
    def __init__(self,codigo_lector,nombres,apellido_paterno,apellido_materno,dni,edad,telefono):
        self.codigo_lector = codigo_lector
        self.nombres = nombres 
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.dni = dni
        self.edad = edad
        self.telefono = telefono 

    def __str__(self):
        rpta = self.codigo_lector+" - "+self.nombres+" "+self.apellido_paterno+" "+self.apellido_materno
        return rpta
        

class Libros: 
    def __init__(self,codigo_libro,titulo,autor,categoria,paginas,descripcion):
        self.codigo_libro = codigo_libro
        self.titulo = titulo 
        self.autor = autor
        self.categoria = categoria 
        self.paginas = paginas 
        self.descripcion = descripcion 

    def __str__(self):
        rpta = self.codigo_libro+" - "+self.titulo+", "+self.autor
        return rpta

class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(key + color.GREEN + " → " + color.END + value)
            print("")
            ans = input(
                color.YELLOW + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                print("Hasta, pronto ...")
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED + "Opción no valida, escoja una opción valida" + color.END)
                time.sleep(3)
        return ans

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()

#Menu principal 
conn = conexion()
opMenuPrincipal ={"Lector":"1", "Libros":"2","Prestamos":"3","Salir": "0"}
optSubMenu1 = {"Listar Lectores":"1","Registrar Lector":"2","Actualizar Lector":"3","Atras":"0"}
optSubMenu2 = {"Listar Libros":"1","Registrar Libro":"2","Actualizar Libro":"3","Atras":"0"}
optSubMenu3 = {"Listar Prestamos":"1","Alquilar Libro":"2","Devolver Libro":"3","Atras":"0"}

showMenu = True
showLector = True
showLibro = True 
showPrestamo = True

respuesta = ""
rptlector = ""
rptlibros = ""
rptprestamos = ""

menuPrincipal = Menu("Menu Principal", opMenuPrincipal) 

while showMenu:
    respuesta = menuPrincipal.show()
    if (respuesta == "0"):
        print("")
        break
    elif(respuesta == "1"):
        menuLector = Menu("LECTOR", optSubMenu1) 
        while showLector:
            rptlector = menuLector.show()
            if (rptlector == "0"): #atras
                break
            if (rptlector == "1"):
                query = """select * from lector;"""
                result = conn.consultarBDD(query)
                headerlector = ['ID', 'Codigo', 'Nombre', 'Ape.Paterno', 'Ape.Materno',
                      'Dni','Edad', 'Telefono']
                print(tabulate(result, headers=headerlector, tablefmt='fancy_grid'))
                input("presiona cualquier tecla para continuar")
            if (rptlector == "2"):
                codigo = input("Escribe el Codigo de Lector: ")
                nombre = input("Escribe tu nombre: ")
                apellidoPaterno = input("Escribe tu apellido Paterno: ")
                apellidoMaterno = input("Escribe tu apellido Materno: ")
                dni = input("Escribe tu DNI: ")
                edad = input("Escribe tu edad: ")
                telefono = input("Escribe tu telefono: ")
                query = f"""insert into lector (codigo_lector,nombres,apellido_paterno,apellido_materno,dni,edad,telefono) 
                        values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}','{dni}',{edad},'{telefono}');"""
                result = conn.ejecutarBDD(query)

                if (result):
                    print("Se registro correctamente !")
                input("presiona una tecla para continuar...")

            if (rptlector == "3"):           
                query = """Select id_lector,codigo_lector,concat(nombres,' ',apellido_paterno) as nombres from lector;"""
                result = conn.consultarBDD(query)
                print(color.RED + "|ID\t|CODIGO\t|NOMBRES" + color.END)
                for item in result:
                    print(
                        f"|{item[0]}\t|{item[1]}\t|{item[2]}\t")
                print("")
                id = input("Escoje un ID para modificar: ")
                codigo = input("Escribe el Codigo de Lector: ")
                nombre = input("Escribe tu nombre: ")
                apellidoPaterno = input("Escribe tu apellido Paterno: ")
                apellidoMaterno = input("Escribe tu apellido Materno: ")
                dni = input("Escribe tu DNI: ")
                edad = input("Escribe tu edad: ")
                telefono = input("Escribe el telefono: ")
                query = f"""update lector
                            set codigo_lector = '{codigo}',
                            nombres = '{nombre}',
                            apellido_paterno = '{apellidoPaterno}',
                            apellido_materno = '{apellidoMaterno}',
                            dni = '{dni}',
                            edad = {edad},
                            telefono = '{telefono}'
                            where id_lector = {id};"""
                result = conn.ejecutarBDD(query)
                if(result):
                    print("Se actualizo correctamente !!")
                input("presiona una tecla para continuar...")


    elif(respuesta == "2"):
        menuLibros = Menu("LIBROS", optSubMenu2) 
        while showLibro:
            rptlibros = menuLibros.show()
            if (rptlibros == "0"): #atras
                break
            if (rptlibros == "1"):
                query = """select id_libro,codigo_libro,condicion,titulo, autor, categoria, paginas, editorial  from libros order by condicion asc;"""
                resultlibros = conn.consultarBDD(query)
                headerlibros = ['ID', 'Codigo','Condicion','Titulo', 'Autor', 'Categoria',
                      'Paginas','Editorial']
                print(tabulate(resultlibros, headers=headerlibros, tablefmt='fancy_grid'))
                input("presiona cualquier tecla para continuar")
            if (rptlibros == "2"):
                codigo = input("Escribe el Codigo del Libro: ")
                titulo = input("Escribe tu nombre: ")
                autor = input("Escribe tu apellido Paterno: ")
                categoria = input("Escribe tu apellido Materno: ")
                paginas = str(input("Escribe tu DNI: "))
                editorial = input("Escribe tu edad: ")
                condicion = input("Escribe tu telefono: ")
                query = f"""insert into libros (codigo_libro,titulo,autor,categoria,paginas,editorial,condicion) 
                        values ('{codigo}','{nombre}','{apellidoPaterno}','{apellidoMaterno}','{dni}',{edad},'{telefono}');"""
                result = conn.ejecutarBDD(query)

            if (rptlibros == "3"):
                query = """Select id_libro,codigo_libro,titulo from libros;"""
                result = conn.consultarBDD(query)
                print(color.RED + "|ID\t|CODIGO\t|TITULO|\t" + color.END)
                for item in result:
                    print(
                        f"|{item[0]}\t|{item[1]}\t|{item[2]}\t")
                print("")
                id = input("Escoje un ID para modificar: ")
                codigo = input("Escribe el Codigo de Lector: ")
                autor = input("Escribe tu nombre: ")
                titulo = input("Escribe tu nombre: ")
                categoria = input("Escribe tu apellido Paterno: ")
                paginas = input("Escribe tu apellido Materno: ")
                editorial = str(input("Escribe tu DNI: "))
                condicion = input("Escribe tu edad: ")
                query = f"""update libros
                            set codigo_libro = '{codigo}',
                            titulo = '{nombre}',
                            autor = '{apellidoPaterno}',
                            categoria = '{apellidoMaterno}',
                            paginas = '{dni}',
                            editorial = {edad},
                            condicion = '{telefono}'
                            where id_libro = {id};"""
                result = conn.ejecutarBDD(query)
                if(result):
                    print("Se actualizo correctamente !!")
                input("presiona una tecla para continuar...")

    elif(respuesta=="3"):
        menuPrestamos = Menu("PRESTAMOS", optSubMenu3) 
        while showPrestamo:
            rptprestamos = menuPrestamos.show()
            if (rptprestamos == "0"): #atras
                break
            if (rptprestamos == "1"):
                query = """ select pe.id_prestamo,l.titulo,le.nombres, pe.alquilado, pe.devuelto
                                from prestamos pe 
                                inner join libros l on l.id_libro = pe.id_libro
                                inner join lector le on le.id_lector = pe.id_lector  ;"""
                result = conn.consultarBDD(query)
                headerlector = ['ID', 'Lector', 'Libro', 'Fecha Alquiler', 'Fecha Devolucion']
                print(tabulate(result, headers=headerlector, tablefmt='fancy_grid'))
                input("presiona cualquier tecla para continuar")

            if (rptprestamos == "2"):
                query = """Select id_libro,codigo_libro,titulo from libros where condicion='LIBRE';"""
                result = conn.consultarBDD(query)
                print("LIBRES para alquilar")
                print("")
                print(color.RED + "|ID\t|CODIGO\t|TITULO\t" + color.END)
                for item in result:
                    print(
                        f"|{item[0]}\t|{item[1]}\t|{item[2]}\t")
                print("")
                idlibro = input("Ingrese el id del libro a alquilar: ")
                dni = input("Ingrese su dni: ")
                query = f"""Select id_lector from lector where dni='{dni}';"""
                resultdni = conn.consultarBDD(query)

                querylibro = f"""Select condicion from libros where id_libro={idlibro} and condicion='LIBRE'"""
                resultlibro = conn.consultarBDD(querylibro)

                if (resultdni):
                    if (resultlibro):
                        for item in resultdni:
                            idlector=item[0]
                            query1 = f"""insert into prestamos (id_lector,id_libro,alquilado) values ({idlector},{idlibro},now());"""
                            result1 = conn.ejecutarBDD(query1)
                            if (result1):
                                print("Se realizo el prestamo correctamente")
                    
                            query2 = f"""update libros set condicion = 'PRESTADO' where id_libro = {idlibro} and condicion='LIBRE';"""
                            result2 = conn.ejecutarBDD(query2)
                            if (result2):
                                print("El libro se alquilo !!")
                                print("")
                    else:
                        print(color.RED+"El libro ya se encuentra alquilado o el id del libro es incorrecto"+color.END)
                        print("")
                else:
                    print(color.RED+"No se encuentra registrado como Lector"+color.END)
                    print("")
                input("presiona una tecla para continuar...")

            if (rptprestamos == "3"):
                dni = input("Ingrese su dni: ")
                query = f"""Select id_lector from lector where dni='{dni}';"""
                resultdni = conn.consultarBDD(query)
                if (resultdni):
                    for item in resultdni:
                        idlector=item[0]
                        query5 = f"""Select id_libro,codigo_libro,titulo from libros where id_libro in (Select id_libro from prestamos where id_lector='{idlector}');"""
                        resultlibro = conn.consultarBDD(query5)
                        print(color.RED + "|ID\t|CODIGO\t|TITULO\t" + color.END)
                        for item in resultlibro:
                            print(f"|{item[0]}\t|{item[1]}\t|{item[2]}\t")

                        idlibro = input('Ingrese el ID del libro a devolver: ')
                        queryprestamo = f"""Select id_prestamo from prestamos where id_libro={idlibro} and id_lector={idlector};"""
                        resultprestamo = conn.consultarBDD(queryprestamo)
                        if (resultprestamo):
                            query1 = f"""update prestamos
                                        set devuelto = now()
                                        where id_libro = {idlibro} and id_lector={idlector};"""
                            result1 = conn.ejecutarBDD(query1)
                            if(result1):
                                print("Se realizo la devolucion correctamente !!")
                                    
                            query2 = f"""update libros
                                        set condicion = 'LIBRE'
                                        where id_libro = {idlibro};"""
                            result2 = conn.ejecutarBDD(query2)
                            if(result2):
                                print("El libro se encuentra devuelto") 
                        else:
                            print(color.RED+"El id del libro es incorrecto"+color.END)
                            print("")       
                else:
                    print(color.RED+"No se encuentra registrado como Lector"+color.END)
                    print("")
                input("presiona una tecla para continuar...")

