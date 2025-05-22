import sys
import os
from src.api_main.infraestructure.scheduler.task_scheduler import start_scheduler
from src.api_main.utils.login_required_util import login_required
from src.api_main.utils.auth_utils import validate_jwt_token
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.api_main.infraestructure.database import init_db, engine
from src.api_main.config import Config
from src.api_main.interface.http import user_ns
from src.api_main.interface.http.swagger_config import api
from flask_cors import CORS
from src.api_main.interface.http.routes.frontend_routes import frontend_bp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

scheduler = start_scheduler()

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:5000"}})

app.secret_key = secret_key

app.config.from_object(Config)

api.add_namespace(user_ns)

api.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(frontend_bp)

init_db(engine)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
