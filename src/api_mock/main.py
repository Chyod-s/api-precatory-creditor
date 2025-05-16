from flask import Flask
from src.api_mock.config import Config
from src.api_mock.views.certificate_view import certificate_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(certificate_bp)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
