from flask_restx import reqparse

pregatory_parse = reqparse.RequestParser()
pregatory_parse.add_argument("credor_id", type=str, required=True, location="form", help="Id do credor")
pregatory_parse.add_argument("numero_precatorio", type=str, required=False, location="form", help="Número do precatório")
pregatory_parse.add_argument("valor_nominal", type=float, required=False, location="form", help="Valor nominal do precatório")
pregatory_parse.add_argument("foro", type=str, required=False, location="form", help="Foro do precatório")
pregatory_parse.add_argument("data_publicacao", type=str, required=False, location="form", help="Data de publicação do precatório")
