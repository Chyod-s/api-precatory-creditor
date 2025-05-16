from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

certificate_parser = reqparse.RequestParser()
certificate_parser.add_argument(
    "arquivo_url",
    location="files",
    type=FileStorage, 
    required=True,
    help="Arquivo para upload"
)
certificate_parser.add_argument(
    "tipo",
    type=str,
    required=True,
    help="Tipo do documento"
)
certificate_parser.add_argument(
    "origem",
    type=str,
    required=True,
    help="Origem do documento"
)
certificate_parser.add_argument(
    "status",
    type=str,
    required=True,
    help="Status do documento"
)
certificate_parser.add_argument(
    "recebida_em",
    type=str,
    required=True,
    help="Data de recebimento no formato YYYY-MM-DD"
)
