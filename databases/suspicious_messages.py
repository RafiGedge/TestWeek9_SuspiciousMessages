from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databases.models import Base, Email
from databases.settings import postgres_url as db_url

engine = create_engine(db_url)
session_maker = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def insert_email(email: Email):
    new_email = Email(email=email.email,
                      username=email.username,
                      ip_address=email.ip_address,
                      created_at=email.created_at,
                      location=email.location,
                      device_info=email.device_info,
                      sentences=email.sentences)
    with session_maker() as session:
        session.add(new_email)
        session.commit()
    print(f'Suspicious messages Inserted.')
