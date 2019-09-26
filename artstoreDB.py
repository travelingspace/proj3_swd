from peewee import *

#refrence the artstore database and assign it to a variable we can use to connect to in the base model class
db = SqliteDatabase('artstore.sqlite')

#peewee documentation states to use this pattern of creating a base model super class which uses the DB specified above. This is to ensure that the correct
#db is always used for child classes that inherit from the base model super class
class BaseModel(Model):
    class Meta:
        database = db
#===============================================================================================================

class Artist(BaseModel):
    name = CharField(unique=True)
    email = CharField()

        
class Artwork(BaseModel):
    artistID = ForeignKeyField(Artist)
    artwork_name = CharField(unique=True)
    price = DecimalField(decimal_places=2)
    is_available = BooleanField

db.connect()
db.create_tables([Artist, Artwork])

def addArtist(name,email):
    
    try:
        with db.atomic():
            Artist.create(
                name=name,
                email=email)

            print("Success creating new artist.")

    except IntegrityError:
        print('Unable to add artist. Name must be unique. Please try again')

def getAllArtByArtist(Artist):
    
    try:
        with db.atomic():
            artworks = Artwork.select().join(Artist)
            
            if artworks.count == 0:
                print("No artworks currently in stock by: ", Artist.name)
            
            for aw in artworks:
                print(aw)

    except:
        print("An error has occured. Try again.")

