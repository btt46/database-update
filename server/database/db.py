import sqlite3
from service import *

class DataBase():
    def __init__(self, db_path, db_schema):
        self.db_path = db_path
        self.db_schema = db_schema

    def init_db(self):
        conn = create_connection(self.db_path)
        cur = conn.cursor()

        with open(self.db_schema) as fp:
            cur.executescript(fp.read())
        
        conn.commit()
        conn.close()

if __name__ == "__main__":
    database = DataBase('./database/users.db', './database/schema.sql')

    # Initialize a dabase
    database.init_db()

    # Add the csv file to database 
    # !!! (optional) or ( there are no data in the database
    users_csv_to_db("./database/users.db", "./database/Data/data.csv")