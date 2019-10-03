from peewee import *
from Model import model
from SQL_db import artstoreDB
from SQL_db import config as conn 

#peewee documentation states to use this pattern of creating a base model super class which uses the DB specified above. This is to ensure that the correct
#db is always used for child classes that inherit from the base model super class
class BaseModel(Model):
    
    def initialize_DB(self):

        try:
            #check if the class tables exist in the artstore db, and if not, create them
            c = conn.db.cursor()
                        
            #get the count of tables with the name artist
            c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''', 'artist')

            #if the count is 1, then table exists, no need to create it
            if c.fetchone()[0]==1 : {
                
            } 
            else:
                conn.db.create_tables([model.Artist])
                        
            #get the count of tables with the name artwork
            c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''', 'artwork')

            #if the count is 1, then table exists, no need to create it
            if c.fetchone()[0]==1 : {
                
            } 
            else:
                conn.db.create_tables([model.Artwork])

            #close the connection
            conn.db.close()

            return True
            
        except sqlite3.Error as e:
            print("Error connecting to the DB: ", e )
            return False
    
    class Meta:
        database = conn.db
#===============================================================================================================

    def addArtist(self, name, email):
        
        try:
            with conn.db.atomic() as db:
                artist = db.create(
                    name=name,
                    email=email)

                return(artist)

        except IntegrityError:
            print('Unable to add artist. Name must be unique. Please try again')

    #gets all artwork records associated to the Artist object
    def getAllArtByArtist(self):

        try:
            with conn.db.atomic() as db:
                
                artworks = db.Artwork.select().join(db.artwork.Artwork, on=(self.ROWID == db.artwork.Artwork.artistID))
                
                if artworks.count == 0:
                    print("No artworks currently in stock by: ", self.name)
                    return
                else:
                    return(artworks)

        except sqlite3.Error as e:
            print("An error has occured: ", e)


