from flask_restx import Namespace, Resource
from src.api_main.interface.http.controllers.pregatory_controller import create_precatory
from src.api_main.interface.http.controllers.aggregate_controller import find_aggregate
from src.api_main.interface.http.swagger import certificate_parser, create_user_parser, login_user_parser, creditor_parser, personal_document_parser, find_certificate_parser, pregatory_parse
from src.api_main.interface.http.controllers.certificate_controller import certificate_personal_document, find_certificates
from src.api_main.interface.http.controllers.personal_document_controller import create_personal_document
from src.api_main.interface.http.controllers.creditor_controller import create_creditor, get_creditor
from src.api_main.interface.http.controllers.user_controller import create_user, get_user
from flask_jwt_extended import jwt_required

user_ns = Namespace('backend-challenge', description='API features for users')

@user_ns.route('/login')
@user_ns.expect(login_user_parser)
class LoginUserResource(Resource):
    def post(self):
        args = login_user_parser.parse_args()
        response = get_user(args)
        return response

@user_ns.route('/register')
class CreateUserResource(Resource):
    @user_ns.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        response, status_code = create_user(args)
        return response, status_code

@user_ns.route('/creditors')
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

@user_ns.route('/documents')
class PersonalDocumentResource(Resource):
    @jwt_required()
    @user_ns.expect(personal_document_parser)
    def post(self):
        args = personal_document_parser.parse_args()
        response, status_code = create_personal_document(args)
        return response, status_code

@user_ns.route('/certificates')
class CertificateResource(Resource):
    @jwt_required()
    @user_ns.expect(certificate_parser)
    def post(self):
        args = certificate_parser.parse_args()
        response, status_code = certificate_personal_document(args)
        return response, status_code

@user_ns.route('/users/<int:user_id>/summary')
class CreditorUserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        response = find_aggregate(user_id)
        return response

@user_ns.route('/users/<int:user_id>/creditors')
class GetCreditorUserResource(Resource):
    @jwt_required()
    def get(self, user_id): 
        response, status_code = get_creditor(user_id)
        return response, status_code

@user_ns.route('/precatory')
class PregatoryUserResource(Resource):
    @jwt_required()
    @user_ns.expect(pregatory_parse)
    def post(self):
        args = pregatory_parse.parse_args()
        response, status_code = create_precatory(args)
        return response, status_code
    