class CustomAPIException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """Retorna a exceção como um dicionário para resposta JSON."""
        return {
            "status": "error",
            "message": self.message
        }
    
    def __str__(self):
        return self.message
