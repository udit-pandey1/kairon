from datetime import datetime

from mongoengine import Document, StringField, LongField, DateTimeField, BooleanField, SequenceField


class User(Document):
    email = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True)
    role = StringField(required=True, default="trainer")
    is_integration_user = BooleanField(default=False)
    account = LongField(required=True)
    bot = StringField(required=True)
    user = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    status = BooleanField(default=True)


class Bot(Document):
    name = StringField(required=True)
    account = LongField(required=True)
    user = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    status = BooleanField(default=True)


class Account(Document):
    id = SequenceField(required=True, primary_key=True)
    name = StringField(required=True)
    user = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    status = BooleanField(default=True)
