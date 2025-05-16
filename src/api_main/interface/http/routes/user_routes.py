from flask_restx import Namespace, Resource
from src.api_main.interface.http.swagger import create_user_parser, login_user_parser
from src.api_main.interface.http.swagger import certificate_parser
from src.api_main.interface.http.controllers.certificate_controller import certificate_personal_document
from src.api_main.interface.http.controllers.personal_document_controller import create_personal_document
from src.api_main.interface.http.controllers.creditor_controller import create_creditor
from src.api_main.interface.http.controllers.user_controller import create_user, get_user
from flask_jwt_extended import jwt_required

user_ns = Namespace('user', description='Operações relacionadas ao usuário')

@user_ns.route('/user')
class UserResource(Resource):
    @user_ns.expect(login_user_parser)
    def get(self):
        args = login_user_parser.parse_args()
        response, status_code = get_user(args)
        return response, status_code

    @user_ns.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        response, status_code = create_user(args)
        return response, status_code

@user_ns.route('/creditor')
class CreditorResource(Resource):
    @jwt_required()
    def post(self):
        return create_creditor()

@user_ns.route('/personal_document')
class PersonalDocumentResource(Resource):
    @jwt_required()
    def post(self):
        return create_personal_document()

@user_ns.route('/certificate')
class CertificateResource(Resource):
    @jwt_required()
    @user_ns.expect(certificate_parser)
    def post(self):
        args = certificate_parser.parse_args()
        response, status_code = certificate_personal_document(args)
        return response, status_code
