import sqlite3

conn = sqlite3.connect("db/database.db")
cursor = conn.cursor()

cursor.execute('''
    create table users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        dtcreate TIMESTAMP
    );''')

conn.commit()
cursor.close()
conn.close()