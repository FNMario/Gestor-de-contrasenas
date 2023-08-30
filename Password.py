from Connection import *

def register_entry(name, url, username, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''INSERT INTO password (
            name, url, username, password, description)
            VALUES (?, ?, ?, ?, ?)'''
        data = (name, url, username, password, description)
        cursor.execute(sql_sentence, data)
        connection.commit()
        connection.close()
        return 'Correct registration.'
    except Error as err:
        return 'An error has occurred: ' + str(err)
    
def print_entries():
    data = []
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''SELECT * FROM password'''
        cursor.execute(sql_sentence)
        data = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred: ' + str(err))
    return data

def find_entry(id):
    data = []
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''SELECT * FROM password WHERE id=?'''
        cursor.execute(sql_sentence, (id,))
        data = cursor.fetchall()
        connection.close()
    except Error as err:
        print('An error has occurred: ' + str(err))
    return data

def change_entry(id, name, url, username, password, description):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''UPDATE password SET name=?, url=?,
        username=?, password=?, description=? WHERE id=?'''
        data = (name, url, username, password, description, id)
        cursor.execute(sql_sentence, data)
        connection.commit()
        connection.close()
        return 'A password has been modified'
    except Error as err:
        return 'An error has occurred: ' + str(err)
    
def delete_entry(id):
    try:
        connection = connect()
        cursor = connection.cursor()
        sql_sentence = '''DELETE FROM password WHERE id=?'''
        cursor.execute(sql_sentence, (id,))
        connection.commit()
        connection.close()
        return 'A password has been deleted'
    except Error as err:
        return 'An error has occurred: ' + str(err)
