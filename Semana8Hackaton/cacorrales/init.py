import utils.utils 
from views import registros 
from orator import Model,DatabaseManager
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


listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamo":2}
menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

resMenuInicial = menuInicial.mostrarMenu()
stopMenu = True
while stopMenu:
    if(resMenuInicial == 1):
        log.info("Modulo de Registro")
        objRegistros = registros.Registros()
        objRegistros.registroLibros()
        stopMenu = False
    if(resMenuInicial == 2):
        log.info("Modulo de Prestamo")

    elif(resMenuInicial == 9):
        log.info("Saliendo")
        stopMenu = False
