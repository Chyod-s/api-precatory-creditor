from flask import Blueprint
from ..controllers.user_controller import create_user

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['POST'])(create_user)
