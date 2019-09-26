from peewee import *

db = SqliteDatabase('artstore.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db # This model uses the "artstore.db" database.

class Artwork(Model):
    artistID = ForeignKeyField(Artist)
    artwork_name = CharField()
    price = DecimalField(decimal_places=2)
    is_available = BooleanField

    class Meta:
        database = db # This model uses the "artstore.db" database.



db.connect()
db.create_tables([Artwork])



