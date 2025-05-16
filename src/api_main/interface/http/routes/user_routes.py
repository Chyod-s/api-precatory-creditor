from flask import Blueprint
from src.api_main.interface.http.controllers.creditor_controller import create_creditor
from src.api_main.interface.http.controllers.user_controller import create_user, get_user
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['POST'])(create_user)

user_bp.route('/user', methods=['GET'])(get_user)

user_bp.route('/creditor', methods=['POST'])(jwt_required()(create_creditor))
