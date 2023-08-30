import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def connect():
    try:
        connection = sqlite3.connect('database.db')
        return connection
    except Error as err:
        print(err)
    
def create_tables(connection):
    cursor = connection.cursor()
    sentence_sql1 = ''' CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        master_password TEXT NOT NULL
    )'''
    sentence_sql2 = ''' CREATE TABLE IF NOT EXISTS password (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        description TEXT
    )'''

    cursor.execute(sentence_sql1)
    cursor.execute(sentence_sql2)
    connection.commit()