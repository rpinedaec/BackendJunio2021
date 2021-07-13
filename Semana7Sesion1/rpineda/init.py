import pymongo
from pymongo import collection
from conexion import Conexion

# cliente = pymongo.MongoClient("mongodb://localhost:27017")
# print(cliente)
# db = cliente.mundial
# print(db)

class Mobile():
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
    def toDic(self):
        return self.__dict__
    def __str__(self) -> str:
        return {'modelo': self.modelo, 'precio':self.precio}

# try:
#     cliente = pymongo.MongoClient("localhost", 27017)
#     print(cliente)
#     db = cliente.mundial
#     db = cliente["mundial"]
#     print(db)

#     coleccion = db.paises.africa
#     data = {
#         'nombre': 'Roberto',
#         'apellido': 'Pineda'
#     }

#     result = coleccion.insert_one(data)
#     data2 = [{"nombre": "Karen", "apellido": "Lam"},
#              {"nombre": "David", "apellido": "Lopez"},
#              {"nombre":"Juan", "email":"rpineda@x-codec.net"}
#              ]
#     result = coleccion.insert_many(data2)
#     print(result.inserted_ids)


# except pymongo.errors.ConfigurationErr as error:
#     print(f"Hubo un error en la conexion: {str(error)}")

celular = Mobile("Samsung",1000)
conn = Conexion()
result = conn.insertarRegistro("celular",celular.toDic())
print(result)