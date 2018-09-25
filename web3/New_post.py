from mongoengine import Document, StringField, IntField, FloatField

class Post(Document):
    name = StringField()
    email = StringField()
    log_in = StringField()
    password = StringField()
    