from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)   

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Pachaqtec 2"

@app.route('/hola')
def hola():
    return "Hola desde Ruta"

#HAer una ruta Post
#hacer una ruta Patch
#hacer una ruta Put
#hacer una ruta Delete

if __name__ == "__main__":
    app.run()