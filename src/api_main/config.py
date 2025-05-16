import os

class Config:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5002
    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_DELTA_SECONDS = 3600  