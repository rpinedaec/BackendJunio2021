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
        'password': 'pachaqtec2021'
    }
}
db = DatabaseManager(config)
Model.set_connection_resolver(db)


log = utils.utils.log("INIT")
log.info("Inicando programa")


listaMenu = {"\t- Modulo de Registo":1,"\t- Modulo de Prestamos":2}
menuInicial =  utils.utils.Menu("Menu Principal",listaMenu)

resMenuInical = menuInicial.mostrarMenu()
stopMenu = True
while stopMenu:
    if(resMenuInical == 1):
        log.info("Entrando al Modulo de Registro")
        objRegistros = registros.Registros()
        objRegistros.registroLibros()
        stopMenu = False
    elif(resMenuInical == 9):
        log.info("Saliendo")
        stopMenu = False
