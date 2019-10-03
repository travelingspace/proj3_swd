from peewee import SqliteDatabase

#refrence the artstore database and assign it to a variable we can use to connect to in the base model class
db = SqliteDatabase('artstore.sqlite')