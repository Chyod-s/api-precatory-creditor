from src.api_main.interface.http.swagger.certificate.certificate_parser import certificate_parser
from src.api_main.interface.http.swagger.users.create_user_parse import create_user_parser
from src.api_main.interface.http.swagger.users.login_user_parse import login_user_parser
from src.api_main.interface.http.swagger.creditor.creditor import creditor_parser
from src.api_main.interface.http.swagger.personal_document.personal_document_parse import personal_document_parser
from src.api_main.interface.http.swagger.certificate.find_certificate_parser import find_certificate_parser
from src.api_main.interface.http.swagger.pregatory.pregatory_parse import pregatory_parse

__all__ = [
    "certificate_parser",
    "create_user_parser",
    "login_user_parser",
    "creditor_parser",
    "personal_document_parser",
    "find_certificate_parser",
    "pregatory_parse"
]