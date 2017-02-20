from peewee import *
from super_sprinter_3000.connectdatabase import ConnectDatabase


class Status(Model):
    name = CharField()

    class Meta:
        database = ConnectDatabase.db
