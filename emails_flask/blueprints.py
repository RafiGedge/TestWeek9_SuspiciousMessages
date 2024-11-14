from flask import Blueprint, request, jsonify

from databases.all_messages import insert_message
from databases.suspicious_messages import insert_email
from emails_kafka.producer import send_message
from databases.models import Email

app_bp = Blueprint('app', __name__)


@app_bp.route('/email', methods=['POST'])
def get_email():
    data = request.get_json()
    email = Email(**data)
    send_message(email.sentences)
    insert_message(data)
    insert_email(email)
    return jsonify({'message': 'hi'}), 200
