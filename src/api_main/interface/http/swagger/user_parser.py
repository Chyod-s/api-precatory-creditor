from flask_restx import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('user_name', type=str, required=True, location='json', help='Nome do usuário')
user_parser.add_argument('password', type=str, required=True, location='json', help='Senha do usuário')
