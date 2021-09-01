from sqlalchemy.orm import backref
from app import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    producto = db.relationship('Producto', backref='product', lazy='dynamic')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    stock = db.Column(db.Integer)
    precio = db.Column(db.Numeric(10,2))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    @staticmethod
    def get_all():
        return Producto.query.all()
    @staticmethod
    def insertProduct(nombre,stock,precio,categoria):
        #insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
        producto = Producto(nombre = nombre,stock = stock,precio = precio,categoria_id = categoria)
        db.session.add(producto)
        db.session.commit()
        return 0
        
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    dni = db.Column(db.String(10))
    recibo = db.relationship('Recibo', backref='recib', lazy='dynamic')

class Recibo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), index=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    
    @staticmethod
    def get_all():
        return Producto.query.all()