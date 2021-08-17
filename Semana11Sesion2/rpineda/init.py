import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, request
from flask_restplus import Resource, Api
from werkzeug.utils import cached_property

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)  

@api.route('/hello')                   #  Create a URL route to this resource
class HelloWorld(Resource):            #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        return {'hello': 'world'}





if __name__ == '__main__':
    app.run()