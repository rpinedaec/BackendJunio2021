from pymongo import MongoClient, errors


class Conexion():
    def conexion(self):
        uri = 'mongodb://localhost:27017'
        database = 'Mobile'
        try:
            conn = MongoClient(uri)
            db = conn[str(f"{database}")]
            return db
        except Exception as error:
            return False

   
    def insertarRegistro(self, collection, data):
        conexion = self.conexion()
        doc = conexion[str(f"{collection}")]
        res = doc.insert_one(data).inserted_id
        return res