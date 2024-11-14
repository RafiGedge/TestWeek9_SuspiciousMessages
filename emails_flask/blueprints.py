from flask import Blueprint, request, jsonify

from model import Email

app_bp = Blueprint('app', __name__)


@app_bp.route('/email', methods=['POST'])
def get_email():
    data = request.get_json()
    email = Email(**data)

    return jsonify({'message': 'hi'}), 200
