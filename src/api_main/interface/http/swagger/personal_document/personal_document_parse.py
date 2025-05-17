from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

personal_document_parser = reqparse.RequestParser()
personal_document_parser.add_argument('tipo', type=str, required=True, location='form', help='Tipo do documento')
personal_document_parser.add_argument('arquivo_url', type=FileStorage, required=True, location='files', help='URL do arquivo')
personal_document_parser.add_argument('enviado_em', type=str, required=True, location='form', help='Enviado em (YYYY-MM-DD)') 
