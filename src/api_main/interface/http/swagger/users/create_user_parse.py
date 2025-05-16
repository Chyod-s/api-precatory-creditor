from flask_restx import reqparse

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('user_name', type=str, required=True, location='json', help='Nome do usuário')
create_user_parser.add_argument('password', type=str, required=True, location='json', help='Senha do usuário')
