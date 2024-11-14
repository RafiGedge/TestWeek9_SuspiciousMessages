from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Email(db.Model):
    __tablename__ = 'email'  # noqa
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    location = db.Column(db.JSON)
    device_info = db.Column(db.JSON)
    sentences = db.Column(db.JSON)
