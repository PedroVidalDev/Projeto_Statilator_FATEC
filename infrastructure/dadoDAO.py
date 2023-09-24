import sqlite3
import datetime

def registrarDado(user, dado):
    try:     
        conn = sqlite3.connect('db/database.db')
        cursor = conn.cursor()
        cursor.execute(f"insert into casos_{user[1]} (name, dtcreate) values (?,?)", (dado, datetime.datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        return False

def read(user):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute(f"select * from casos_{user[1]}")
    casos = cursor.fetchall()
    cursor.close()
    conn.close()
    return casos

def deletar(user):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute(f"delete from casos_{user[1]}")
    conn.commit()
    cursor.close()
    conn.close
    return True

def readPareto(user):
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute(f"select name from casos_{user[1]}")
    casos = cursor.fetchall()
    cursor.close()
    conn.close()
    return casos