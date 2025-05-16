from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.api_main.infraestructure.database import init_db, engine
from src.api_main.config import Config
from src.api_main.interface.http import blueprints
import os

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.secret_key = secret_key

app.config.from_object(Config)

jwt = JWTManager(app)

for blueprint in blueprints:
    app.register_blueprint(blueprint, url_prefix="/api")

init_db(engine) 

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
