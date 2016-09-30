from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django_mongoengine import Document, fields, EmbeddedDocument

class User(Document):
    username = fields.StringField(max_length=20)
    password = fields.StringField(max_length=20)
    token = fields.StringField(max_length=128)

class Service(Document):
    name = fields.StringField(max_length=50)

class Options(EmbeddedDocument):
    access_key = fields.StringField()
    droplets = fields.ListField(fields.StringField(required=False))
    size = fields.StringField()
    region = fields.StringField()
    image = fields.StringField()
    state = fields.StringField()

class Setup(Document):
    service = fields.StringField(max_length=50)
    cloud = fields.StringField(max_length=50)
    options = fields.EmbeddedDocumentField(Options, required=False)
