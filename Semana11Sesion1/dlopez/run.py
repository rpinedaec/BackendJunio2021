import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, request
from flask_orator import Orator, jsonify
from orator.orm import belongs_to, has_many, belongs_to_many


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
    pass


@app.route('/users', methods=['POST','GET'])
def create_user():
    #users = User.all()
    #user = User.find(2)
    #user = User.where('city', '=', 'Chiclayo').count()
    users = db.table('users').select('name as user_name').get()
    return jsonify(users)

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
