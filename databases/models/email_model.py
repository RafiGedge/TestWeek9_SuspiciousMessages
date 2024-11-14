from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Email(Base):
    __tablename__ = 'email'  # noqa
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location = Column(JSON)
    device_info = Column(JSON)
    sentences = Column(JSON)
