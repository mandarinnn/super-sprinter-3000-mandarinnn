from super_sprinter_3000.connectdatabase import ConnectDatabase
from peewee import *
from super_sprinter_3000.models.Status import Status


class Story(Model):
    title = CharField()
    story = TextField()
    criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = ForeignKeyField(Status, related_name='story_status')

    class Meta:
        database = ConnectDatabase.db
