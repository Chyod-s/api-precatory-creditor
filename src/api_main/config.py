import os

class Config:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000

    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_DELTA_SECONDS = 3600  

    JWT_SECRET_KEY = os.getenv('JWT_SECRET')
    JWT_TOKEN_LOCATION = ['headers'] 
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'

    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.pdf'}
    MAX_FILE_SIZE = 5 * 1024 * 1024

    