import conexion
import utils

log = utils.log("INIT")
log.info("Inicio de la aplicacion")

class Mobile():
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
    def toDic(self):
        return self.__dict__
    def __str__(self) -> str:
        return f"{self.modelo} --- {self.precio}"


conn = conexion.conexionBDD(4)
# celular = Mobile("Xiaomi",900)
# conn.insertarRegistro("equipos",celular.toDic())

# Sin codiciones trae todos
# result = conn.leerRegistros("equipos",{})
# for item in result:
#     print(item)

# Condicion IN dentro de la lista []
# result = conn.leerRegistros("equipos",{"precio":{"$in":[1000, 1200, 900]}})
# for item in result:
#     print(item)

#$lt Matches values that are less than a specified value.
# result = conn.leerRegistros("equipos",{"precio":{"$lt":1000}})
# for item in result:
#     print(item)

#$eq Matches values that are equal to a specified value.
# result = conn.leerRegistros("equipos",{"precio":{"$eq":900}})
# for item in result:
#     print(item)

#$gt Matches values that are greater than a specified value.
# result = conn.leerRegistros("equipos",{"precio":{"$gt":900}})
# for item in result:
#     print(item)

#$gte Matches values that are greater than or equal to a specified value.
# result = conn.leerRegistros("equipos",{"precio":{"$gte":900}})
# for item in result:
#     print(item)

#$gte Matches values that are greater than or equal to a specified value.
# result = conn.leerRegistros("equipos",{"precio":{"$nin":[900, 1200]}})
# for item in result:
#     print(item)

# conn.actualizarRegistro("equipos", {"modelo": "Huawei"}, {"precio": 1300})

# result = conn.leerRegistros("equipos",{"precio":{"$nin":[900, 1200]}})
# for item in result:
#     print(item)

conn.eliminarRegistro("equipos", {"modelo": "Xiaomi"} )

result = conn.leerRegistros("equipos",{})
for item in result:
    print(item)