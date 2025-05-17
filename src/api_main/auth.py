from flask import Blueprint, redirect, url_for, session, request, render_template

auth = Blueprint('auth', __name__)

@auth.before_app_request
def check_authentication():
    current_endpoint = request.endpoint or ''

    allowed_routes = ['auth.login', 'home']

    if 'user' not in session and current_endpoint not in allowed_routes:
        return redirect(url_for('home'))

    if 'user' in session and current_endpoint == 'auth.login':
        return redirect(url_for('home'))


@auth.route('/login', methods=['POST'])
def login():
    session['user'] = 'usuario_teste'
    return redirect(url_for('home'))

@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))
