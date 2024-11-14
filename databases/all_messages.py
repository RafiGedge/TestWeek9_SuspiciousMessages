from pymongo import MongoClient

from emails_flask.model import Email

client = MongoClient('localhost', 27017)
db = client['messages']
collection = db['all_messages']


def insert_message(data: Email):
    collection.insert_one(data)
    print(f'Email Inserted: {data['email']}. Sentences {str(data['sentences'])[:25]}...\']')
