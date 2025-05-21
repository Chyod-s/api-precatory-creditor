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



@app.route('/home')
def home():
    token = request.cookies.get('auth_token')
    print(f"Token recebido no /home: {token}")
    
    if token and validate_jwt_token(token):
        print("Token válido, redirecionando para dashboard")
        return redirect(url_for('dashboard'))
    
    print("Token inválido ou não encontrado, redirecionando para login")
    return render_template('pages/login.html') 
        
@app.route('/logout')
def logout():
    response = redirect(url_for('home'))
    response.set_cookie('auth_token', '', max_age=0)
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/credor')
@login_required
def credor():
    return render_template('pages/credor.html')

@app.route('/documentos')
@login_required
def documentos():
    return render_template('pages/documentos_pessoal.html')

@app.route('/precatorio')
@login_required
def precatorio():
    return render_template('pages/precatorio.html')

@app.route('/certidao')
@login_required
def certidao():
    return render_template('pages/certidao.html')

@app.route('/consulta_agregada')
@login_required
def consulta_agregada():
    return render_template('pages/consulta_agregada.html')

@app.route('/register')
def register():
    return render_template('pages/register.html')


init_db(engine)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
