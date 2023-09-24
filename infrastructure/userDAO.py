import sqlite3
import datetime

conn = sqlite3.connect('db/database.db')
cursor = conn.cursor()

def validarUser(email):
    cursor.execute(f"select * from users where email = '{email}'")
    user = cursor.fetchone()
    cursor.close()
    conn.close()   
    return user

def criarUser(name, email, password):
    try:
        cursor.execute(f"select * from users where name='{name}'")
        possibleUser = cursor.fetchone()

        cursor.execute(f"select * from users where email='{email}'")
        possibleEmail = cursor.fetchone()
        
        if(possibleUser is not None or possibleEmail is not None):
            return False
        
        cursor.execute("insert into users (name, email, password, dtcreate) values (?,?,?,?)", (name, email, password, datetime.datetime.now()))
        
        cursor.execute(f'''
        create table casos_{name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            dtcreate TIMESTAMP
        );''')

        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    except:
        return False