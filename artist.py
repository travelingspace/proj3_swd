from peewee import *

db = SqliteDatabase('artists.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

db.connect()
db.create_tables([artists])