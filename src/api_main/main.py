import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from flask import Flask, redirect, render_template, session, url_for
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.api_main.infraestructure.database import init_db, engine
from src.api_main.config import Config
from src.api_main.interface.http import user_ns
from src.api_main.interface.http.swagger_config import api
import os

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.secret_key = secret_key

app.config.from_object(Config)

api.add_namespace(user_ns)

api.init_app(app)

jwt = JWTManager(app)

@app.route('/home')
def home():
    print(f"Home - Sessão: {session}") 
    if 'user' in session:
        return redirect(url_for('dashboard_route'))  
       
    return render_template('pages/login.html')  
        

@app.route('/logout')
def logout():
    session.clear()  
    session.modified = True  
    return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')

init_db(engine)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
