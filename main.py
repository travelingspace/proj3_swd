import SQL_db as db

def main():
    
    db = db.artstoreDB()
    db.initialize_DB()

if __name__ == '__main__':

    main()