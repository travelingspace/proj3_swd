from peewee import Model, ModelBase, CharField, ForeignKeyField, DecimalField, BooleanField
from SQL_db import artstoreDB

class Artist(artstoreDB.BaseModel):
    name = CharField(unique=True)
    email = CharField()

    def _init_(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.email} email'

    def __repr__(self):
        return f'Name: {self.name}, Email: {self.email}'

class Artwork(artstoreDB.BaseModel):
    
    artistID = ForeignKeyField(Artist)
    artwork_name = CharField(unique=True)
    price = DecimalField(decimal_places=2)
    is_available = BooleanField

    def _init_(self, artwork_name, artistID, is_available):
        self.artwork_name = artwork_name
        self.artistID = artistID
        self.is_available = is_available

    def __str__(self):
        return f'{self.artwork_name}, {self.artistID} artistID, {self.is_available} is_available'

    def __repr__(self):
        return f'Artwork Name: {self.artwork_name}, artistID: {self.artistID}, is_available: {self.is_available}'

    