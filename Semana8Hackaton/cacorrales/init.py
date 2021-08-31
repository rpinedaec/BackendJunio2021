import utils.utils
from utils.utils import log
from utils.utils import Menu
from views import registros 
from orator import Model,DatabaseManager
from models.libro import Libro

config = {
    'mysql': {
        'driver': 'postgres',
        'host': 'localhost',
        'port': 5432,
        'database': 'biblioteca',
        'user': 'postgres',
        'password': 'S0p0rt320'
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


log = utils.utils.log("INIT")
log.info("Inicando programa")

def menuLibro():
    opMenu = {"Registrar Libro": "1", "Listar Libro": "2", "Actualizar Libro": "3", "Buscar Libro": "4", "Salir": "0"}
    showMenu = True
    ansMenu = ""
    menu = Menu("LIBRO", opMenu)
    while showMenu:
        ansMenu = menu.show()
        if(ansMenu == "0"):
            break
        if(ansMenu=="1"):
          #self.__log.info("Ingresando al Registro de Libros")
          #self.__log.info("Entrando al registro de libros")
          nuevoLibro = Libro()
          nombreLibro = input("escriba el nombre del Libro \n")
          descripcion = input("escriba la descricion del Libro \n")













#listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamo":2}
#menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

#resMenuInicial = menuInicial.mostrarMenu()
#stopMenu = True
#while stopMenu:
#    if(resMenuInicial == 1):
#        log.info("Modulo de Registro")
#        objRegistros = registros.Registros()
#        objRegistros.registroLibros()
#        stopMenu = False
#    if(resMenuInicial == 2):
#        log.info("Modulo de Prestamo")

#    elif(resMenuInicial == 9):
#        log.info("Saliendo")
#        stopMenu = False
