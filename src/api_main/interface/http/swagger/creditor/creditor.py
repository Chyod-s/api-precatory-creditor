from flask_restx import reqparse

creditor_parser = reqparse.RequestParser()
creditor_parser.add_argument("nome", type=str, required=True, location="form", help="Nome do credor")
creditor_parser.add_argument("cpf_cnpj", type=str, required=True, location="form", help="CPF ou CNPJ do credor")
creditor_parser.add_argument("email", type=str, required=True, location="form", help="Email do credor")
creditor_parser.add_argument("telefone", type=str, required=True, location="form", help="Telefone do credor")

creditor_parser.add_argument("numero_precatorio", type=str, required=False, location="form", help="Número do precatório")
creditor_parser.add_argument("valor_nominal", type=float, required=False, location="form", help="Valor nominal do precatório")
creditor_parser.add_argument("foro", type=str, required=False, location="form", help="Foro do precatório")
creditor_parser.add_argument("data_publicacao", type=str, required=False, location="form", help="Data de publicação do precatório")
