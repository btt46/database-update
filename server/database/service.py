import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
import pandas as pd

def create_connection(db_path):
    '''
        *** Input ***
        ・db_path: direct path to database
        ・For example: db_path = 'XXXX.db'

        *** Output ***
        return conn
    '''
    conn = None
    try: 
        conn = sqlite3.connect(db_path)
    except Error as err:
        print(err)
    return conn

def select_all(db_path, table_name):
    conn = create_connection(db_path)
    c = conn.cursor()
    
    rows = c.execute("SELECT * FROM {};".format(table_name))

    data = []
    for row in rows.fetchall():
        data.append(row)
    conn.commit()
    conn.close()

    return data

def select_with_key(db_path, table_name, key_name, key_value):
    conn = create_connection(db_path)
    c = conn.cursor()
    key_value = key_value.lower()   # optional
    
    rows = c.execute("SELECT * FROM {} WHERE {} = {} ;".format(table_name, key_name, key_value))
    
    data = []
    for row in rows.fetchall():
        data.append(row)
    conn.commit()
    conn.close()

    return data

def update_data_with_key(db_path, table_name, key_name, key_value,update_data_name, update_value):
    conn = create_connection(db_path)
    c = conn.cursor()
    update_value = update_value.lower() # optional

    #c.execute("update product set price = 2500 where id = 1;")
    c.execute("UPDATE {} set {} = {} where {} = {};".format(table_name, update_data_name, 
                                                            update_value, key_name, key_value))

    conn.commit()
    conn.close()

def users_csv_to_db(db_path, data_path):
    conn = create_connection(db_path)
    c = conn.cursor()

    df = pd.read_csv(data_path)

    num_rows = df.shape[0]

    for i in range(num_rows):
        user_name = df.iloc[i]['name']
        user_tel = df.iloc[i]['tel']
        user_addr = df.iloc[i]['addr']
        user_email = df.iloc[i]['email'].lower()
        user_status = df.iloc[i]['status']
        data = (user_name, user_tel, user_addr, user_email, user_status)

        try:
            c.execute("INSERT INTO USERS VALUES {};".format(str(data)))
        except Error as err:
            print(err, data)

    # Commit and close
    conn.commit()
    conn.close()    
