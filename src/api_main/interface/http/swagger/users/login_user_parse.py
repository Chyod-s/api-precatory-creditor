from flask_restx import reqparse

login_user_parser = reqparse.RequestParser()
login_user_parser.add_argument('user_name', type=str, required=True, location='json', help='Nome do usuário')
login_user_parser.add_argument('password', type=str, required=True, location='json', help='Senha do usuário')
