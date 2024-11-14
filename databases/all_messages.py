from databases.settings import mongo_client as client
from databases.models import Email

db = client['messages_db']
collection = db['all_messages']


def insert_message(data: Email):
    collection.insert_one(data)
    print(f'Email Inserted: {data['email']}. Sentences {str(data['sentences'])[:25]}...\']')
