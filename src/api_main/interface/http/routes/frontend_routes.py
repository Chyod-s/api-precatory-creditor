from flask import Blueprint, render_template, request, redirect, url_for
from src.api_main.utils.login_required_util import login_required
from src.api_main.utils.auth_utils import validate_jwt_token

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/home')
def home():
    token = request.cookies.get('auth_token')
    print(f"Token recebido no /home: {token}")
    
    if token and validate_jwt_token(token):
        print("Token válido, redirecionando para dashboard")
        return redirect(url_for('frontend.dashboard'))
    
    print("Token inválido ou não encontrado, redirecionando para login")
    return render_template('pages/login.html')

@frontend_bp.route('/logout')
def logout():
    response = redirect(url_for('frontend.home'))
    response.set_cookie('auth_token', '', max_age=0)
    return response

@frontend_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard.html')

@frontend_bp.route('/credor')
@login_required
def credor():
    return render_template('pages/credor.html')

@frontend_bp.route('/documentos')
@login_required
def documentos():
    return render_template('pages/documentos_pessoal.html')

@frontend_bp.route('/precatorio')
@login_required
def precatorio():
    return render_template('pages/precatorio.html')

@frontend_bp.route('/certidao')
@login_required
def certidao():
    return render_template('pages/certidao.html')

@frontend_bp.route('/consulta_agregada')
@login_required
def consulta_agregada():
    return render_template('pages/consulta_agregada.html')

@frontend_bp.route('/register')
def register():
    return render_template('pages/register.html')
