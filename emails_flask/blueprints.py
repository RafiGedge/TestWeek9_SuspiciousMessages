from flask import Blueprint, request, jsonify

from emails_kafka.producer import send_message
from model import Email

app_bp = Blueprint('app', __name__)


@app_bp.route('/email', methods=['POST'])
def get_email():
    data = request.get_json()
    email = Email(**data)
    send_message(email.sentences)
    return jsonify({'message': 'hi'}), 200
