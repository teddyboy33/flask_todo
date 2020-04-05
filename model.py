import os
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)


class Task(BaseModel):
    name = CharField(max_length=255, unique=True)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(User, backref='tasks', null=True)

