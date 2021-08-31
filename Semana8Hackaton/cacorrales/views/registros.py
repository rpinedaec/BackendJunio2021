from time import time
from utils.utils import log
from utils.utils import Menu
from models.libro import Libro
from models.autor import Autor
from models.lector import Lector
from models.estadolibro import EstadoLibro
from tabulate import TableFormat, tabulate
import time


class Registros:

    __log = log("Registros")

def menuLibro():
    opMenu = {"Registrar Libro": "1", "Listar Libro": "2", "Actualizar Libro": "3", "Buscar Libro": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("LIBRO", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break
   def registroLibros(self):
#---------- Registra Libro -----------#
        if(ansMenu=="1"):
          self.__log.info("Ingresando al Registro de Libros")
          self.__log.info("Entrando al registro de libros")
          nuevoLibro = Libro()
          nombreLibro = input("escriba el nombre del Libro \n")
          descripcion = input("escriba la descricion del Libro \n")
               
            #autores = Autor()
            #print(f"\t Codigo\t Nombre\t Tipo")
            #for obj in autores.all():
            #   print(f"\t {obj.id}\t {obj.nombre}\t {obj.descripcion}")
            #   print("Escriba el id del Autor de la siguiente lista")
            #   autor_idLibro = input()

            #   estados = EstadoLibro()
            #   print(f"\t Codigo\t Estado")
            #   for obj in estados.all():
            #        print(f"\t {obj.id}\t {obj.descripcion}")
            #   print("Escriba el id del Estado del Libro de la siguiente lista")
            #   estadoLibro = input()
            #   nuevoLibro.nombre = nombreLibro
            #   nuevoLibro.descripcion = descripcion
            #   nuevoLibro.autor_id = autor_idLibro
            #   nuevoLibro.estado_libro_id = estadoLibro
            #   nuevoLibro.save()
            #   stopMenu = False

        if(ansMenu=="2"):
        
            listaLibro = Libro()
            header = ['ID', 'NOMBRE', 'DESCRIPCION','AUTOR_ID','ESTADO_LIBRO_ID']
            print(tabulate(listaLibro, headers=header, tablefmt='fancy_grid'))
              #for obj in listaLibro.all():
               #     print(f"\t {obj.id}\t {obj.nombre}\t {obj.descripcion}\t {obj.autor_id}\t {obj.estado_libro_id}")
               #     print("")
            input("presiona cualquier tecla para continuar")

    def registroLectores(self):
        self.__log.info("Ingresando al Registro de Lector")
        opcionesRegistroLector = {"\t- Registrar Lector":1,"\t- Salir":9}
        menuRegistroLector = Menu("Registro de Libros",opcionesRegistroLector)
        resmenuRegistroLector = menuRegistroLector.mostrarMenu()
        stopMenu = True
        while stopMenu:
            if resmenuRegistroLector == 1:
               self.__log.info("Entrando al registro de lector")
               nuevoLector = Lector()
               nombreLector = input("escriba el nombre del Lector: \n")
               correoLector = input("escriba correo del Lector: \n")
                #autores = Autor()
                #print(f"\t Codigo\t Nombre\t Tipo")
                #for obj in autores.all():
                #    print(f"\t {obj.id}\t {obj.nombre}\t {obj.descripcion}")
               idTipoDocLector = input("Escriba el id Tipo Documento: \n")
               documentoLector = input("Escriba el Numero Documento: \n")
               estadoLector = input("Escriba el Estado del Lector:\n")
                #print(f"\t Codigo\t Estado")
                #for obj in estados.all():
                #    print(f"\t {obj.id}\t {obj.descripcion}")
                #print("Escriba el id del Estado del Libro de la siguiente lista")
                #estadoLibro = input()

               nuevoLector.nombre = nombreLector
               nuevoLector.correo = correoLector
               nuevoLector.idtipodcumento = idTipoDocLector
               nuevoLector.documento = documentoLector
               nuevoLector.estado = estadoLector
               nuevoLector.save()
               stopMenu = False         
            elif resmenuRegistroLector == 9:
               self._log.info("Saliendo")