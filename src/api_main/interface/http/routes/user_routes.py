from flask import Blueprint
from src.api_main.interface.http.controllers.user_controller import create_user

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['POST'])(create_user)
