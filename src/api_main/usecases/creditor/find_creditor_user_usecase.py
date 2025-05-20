from src.api_main.domain.error.exceptions import CustomAPIException
from src.api_main.domain.models.creditor_model import Creditor

class FindCreditorUserUseCase:
    def __init__(self, db):
        self.db = db
    
    def execute(self):
        try:
            creditors = Creditor.get_all_creditors(self.db)

            if not creditors:
                CustomAPIException("Credores não encontrados.", 404)
                
            return creditors
        
        except Exception as e:
            raise CustomAPIException(f"Error retrieving creditors: {str(e)}", 500)
    
    def get_creditor_by_id(self, creditor_id):
        try:
            creditor = Creditor.get_by_credor_id(self.db, creditor_id)

            if not creditor:
                raise CustomAPIException("Credor não encontrado.", 404)
                
            return creditor
        
        except Exception as e:
            raise CustomAPIException(f"Error retrieving creditor: {str(e)}", 500)
        