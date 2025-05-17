from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

find_certificate_parser = reqparse.RequestParser()
find_certificate_parser.add_argument(
    "tipo",
    type=str,
    help="Tipo do documento FEDERAL, STATE, MUNICIPAL ou LABOR"
)
find_certificate_parser.add_argument(
    "origem",
    type=str,
    help="Origem do documento MANUAL ou API"
)
find_certificate_parser.add_argument(
    "status",
    type=str,
    help="Status do documento NEGATIVE, POSITIVE, INVALID ou PENDING"
)
find_certificate_parser.add_argument(
    "recebida_em",
    type=str,
    help="Data de recebimento no formato 2025-05-17"
)
