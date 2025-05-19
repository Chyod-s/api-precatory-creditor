from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

personal_document_parser = reqparse.RequestParser()
personal_document_parser.add_argument('credor_id', type=str, required=True, location='form', help='Id do credor')
personal_document_parser.add_argument('tipo', type=str, required=True, location='form', help='Tipo do documento IDENTIDADE, COMPROVANTE_RESIDENCIA, ETC')
personal_document_parser.add_argument('arquivo_url', type=FileStorage, required=True, location='files', help='Arquivos Permitidos .jpg, .jpeg, .png ou .pdf')
personal_document_parser.add_argument('enviado_em', type=str, required=True, location='form', help='Enviado em 17/05/2025') 