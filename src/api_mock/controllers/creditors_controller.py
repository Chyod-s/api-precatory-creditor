from flask import jsonify
from src.api_mock.models.creditors import creditors

def get_creditors():
    creditors_data = creditors()
    return jsonify(creditors_data), 200