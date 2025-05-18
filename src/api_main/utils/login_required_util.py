from functools import wraps
from flask import request, redirect, url_for
from src.api_main.utils.auth_utils import validate_jwt_token

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token or not validate_jwt_token(token):
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated
