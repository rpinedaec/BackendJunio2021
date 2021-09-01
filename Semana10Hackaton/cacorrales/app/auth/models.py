from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user = db.relationship('User', backref='user', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'<Role {self.name}>'
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Role.query.get(id)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return User.query.all()


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, role_id=1):
        self.name = name
        self.email = email
        self.role_id = role_id


    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return User.query.all()
