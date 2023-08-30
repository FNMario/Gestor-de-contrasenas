import hashlib
from Connection import *

def check_user():
    connection = connect()
    cursor = connection.cursor()
    sql_sentence = 'SELECT * FROM user'
    cursor.execute(sql_sentence)
    user_found = cursor.fetchall()
    connection.close()
    return user_found

def register_user(first_name, last_name, master_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = ''' INSERT INTO user
        (first_name, last_name, master_password)
        VALUES (?, ?, ?)'''
        encrypted_password = hashlib.sha256(master_password.encode('utf-8')).hexdigest()
        data = (first_name, last_name, encrypted_password)
        cursor.execute(sql_sentence, data)
        connection.commit()
        connection.close()
        return 'Successful registration.'
    except Error as err:
        return 'An error has occurred: ' + str(err)

def check_master_password(id, master_password):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''SELECT * FROM user
        WHERE id=? AND master_password=?'''
        encrypted_password = hashlib.sha256(master_password.encode('utf-8')).hexdigest()
        data = (id, encrypted_password)
        cursor.execute(sql_sentence, data)
        data = cursor.fetchall()
        connection.close()
        return data
    except Error as err:
        return 'An error has occurred: ' + str(err)
