from flask_restx import Namespace, Resource
from src.api_main.interface.http.controllers.aggregate_controller import find_aggregate
from src.api_main.interface.http.swagger import certificate_parser, create_user_parser, login_user_parser, creditor_parser, personal_document_parser, find_certificate_parser
from src.api_main.interface.http.controllers.certificate_controller import certificate_personal_document, find_certificates
from src.api_main.interface.http.controllers.personal_document_controller import create_personal_document
from src.api_main.interface.http.controllers.creditor_controller import create_creditor, get_creditor
from src.api_main.interface.http.controllers.user_controller import create_user, get_user
from flask_jwt_extended import jwt_required

user_ns = Namespace('usuarios', description='Operações relacionadas ao usuário')

@user_ns.route('/login-usuarios')
@user_ns.expect(login_user_parser)
class LoginUserResource(Resource):
    def post(self):
        args = login_user_parser.parse_args()
        response = get_user(args)
        return response

@user_ns.route('/register-usuarios')
class CreateUserResource(Resource):
    @user_ns.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        response, status_code = create_user(args)
        return response, status_code

@user_ns.route('/credores')
class CreditorResource(Resource):
    @jwt_required()
    @user_ns.expect(creditor_parser)
    def post(self):
        args = creditor_parser.parse_args()

        precatory_data = {
            "numero_precatorio": args.get("numero_precatorio"),
            "valor_nominal": args.get("valor_nominal"),
            "foro": args.get("foro"),
            "data_publicacao": args.get("data_publicacao"),
        }

        for key in precatory_data.keys():
            args.pop(key, None)

        combined_args = {**args, "precatorio": precatory_data}

        response, status_code = create_creditor(combined_args)
        return response, status_code

@user_ns.route('/documentos')
class PersonalDocumentResource(Resource):
    @jwt_required()
    @user_ns.expect(personal_document_parser)
    def post(self):
        args = personal_document_parser.parse_args()
        response, status_code = create_personal_document(args)
        return response, status_code

@user_ns.route('/certidoes')
class CertificateResource(Resource):
    @jwt_required()
    @user_ns.expect(certificate_parser)
    def post(self):
        args = certificate_parser.parse_args()
        response, status_code = certificate_personal_document(args)
        return response, status_code

@user_ns.route('/buscar-certidoes')
class FindCertificatesUserResource(Resource):
    @jwt_required()
    @user_ns.expect(find_certificate_parser)
    def get(self):
        args = find_certificate_parser.parse_args()
        response, status_code = find_certificates(args)
        return response, status_code
    
@user_ns.route('/buscar-credores')
class CreditorUserResource(Resource):
    @jwt_required()
    def get(self):
        response, status_code = find_aggregate()
        return response, status_code

@user_ns.route('/buscar-credores-by-id/<int:user_id>')
class GetCreditorUserResource(Resource):
    @jwt_required()
    def get(self, user_id): 
        response, status_code = get_creditor(user_id)
        return response, status_code
    