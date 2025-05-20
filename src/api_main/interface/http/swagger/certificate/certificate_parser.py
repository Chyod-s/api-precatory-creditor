from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

certificate_parser = reqparse.RequestParser()
certificate_parser.add_argument(
    "credor_id",
    type=str,
    required=True,
    location='form',
    help="ID do documento"
)
certificate_parser.add_argument(
    "arquivo_url",
    location="files",
    type=FileStorage, 
    required=True,
    help="Arquivos Permitidos .jpg, .jpeg, .png ou .pdf"
)
certificate_parser.add_argument(
    "tipo",
    type=str,
    required=True,
    location='form',
    help="Tipo do documento FEDERAL, STATE, MUNICIPAL ou LABOR"
)
certificate_parser.add_argument(
    "origem",
    type=str,
    required=True,
    location='form',
    help="Origem do documento MANUAL ou API"
)
certificate_parser.add_argument(
    "status",
    type=str,
    required=True,
    location='form',
    help="Status do documento NEGATIVE, POSITIVE, INVALID ou PENDING"
)
certificate_parser.add_argument(
    "recebida_em",
    type=str,
    required=True,
    location='form',
    help="Data de recebimento no formato 17/05/2025"
)
