import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many
from flask_restplus import Resource, Api


env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': os.getenv('DB_SERVER'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASS'),
        'prefix': ''
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Initializing Orator
db = Orator(app)


class User(db.Model):
    __fillable__ = ['name', 'email', 'city']


@app.route('/users', methods=['GET'])
def get_user():
    #users = User.all()
    #user = User.find(2)
    #user = User.where('city', '=', 'Chiclayo').count()
    users = db.table('users').select('name as user_name').get()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.find_or_fail(user_id)
    user.delete()
    return app.response_class('No Content', 204)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user_part(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())
    return jsonify(user)

@app.route('/ciudad')
def getCiudad():
    users = db.table('users').select('city as ciudad').get()
    return jsonify(users)


@app.route('/ciudad/<int:id_ciudad>/<int:id_distrito>')
def getDistrito(id_ciudad=0, id_distrito=0):
    user = User.where('city', '=', 'Chiclayo')
    return "hello"

if __name__ == '__main__':
    app.run()
