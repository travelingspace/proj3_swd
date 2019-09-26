from peewee import *

db = SqliteDatabase('artworks.sqlite')

class Artwork(Model):
    name = CharField()
    email = CharField()

db.connect()
db.create_tables([artworks])