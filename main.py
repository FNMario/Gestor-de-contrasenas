import os
from tabulate import tabulate
import questionary
from Connection import *
import User
import Password

connection = connect()
create_tables(connection)


def check_not_empty(answer):
    if len(answer) > 0:
        return True
    else:
        return 'You must provide a value.'


def home():
    os.system('clear')
    if User.check_user():
        master_password = questionary.password(
            'Enter your master password:', qmark='-').ask()
        check_password = User.check_master_password(1, master_password)
        if len(check_password) == 0:
            questionary.print('Invalid password', style='fg:darkred')
        else:
            print('Welcome!')
            menu()
    else:
        print('Welcome, please register:')
        first_name = questionary.text('First name:',
                                      validate=check_not_empty,
                                      qmark='-').ask()
        last_name = questionary.text('Last name:',
                                     validate=check_not_empty, qmark='-').ask()
        master_password = questionary.password(
            'Master password:', qmark='-').ask()
        answer = User.register_user(first_name, last_name, master_password)
        if answer == 'Successful registration.':
            os.system('clear')
            print(f'Welcome {first_name}')
            menu()
        else:
            print(answer)


def menu():
    while True:
        options = ['Add new entry',
                   'Show me all entries',
                   'Show me one password',
                   'Change one entry',
                   'Delete one entry',
                   'Exit']
        option = questionary.select("What do you want to do?",
                                    choices=options, qmark='-').ask()
        if option == 'Add new entry':
            new_entry()
        elif option == 'Show me all entries':
            show_all_entries()
        elif option == 'Show me one password':
            show_entry_complete()
        elif option == 'Change one entry':
            change_entry()
        elif option == 'Delete one entry':
            delete_entry()
        elif option == 'Exit':
            break
        else:
            print('Invalid option')
            break
        # questionary.confirm('Go back?').ask()
        questionary.select('',choices=['Go back'], qmark='', instruction='(press enter to go back)').ask()
        os.system('clear')
    print('See you later!')


def new_entry():
    questionary.print('New entry', style='bold')
    entry_name = questionary.text('Name:',
                                  validate=check_not_empty, qmark='-').ask()
    username = questionary.text('Username:',
                                validate=check_not_empty, qmark='-').ask()
    password = questionary.text('Password:',
                                validate=check_not_empty, qmark='-').ask()
    description = questionary.text('(optional) Description:', qmark='-').ask()
    url = questionary.text('(optional) url:', qmark='-').ask()
    answer = Password.register_entry(
        entry_name, url, username, password, description)
    print(answer)


def show_all_entries():
    data = Password.print_entries()
    new_data = []
    for item in data:
        item_ = list(item)
        item_[4] = '********'
        new_data.append(item_)
    headers = ['ID', 'NAME', 'URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION']
    table = tabulate(new_data, headers, tablefmt='fancy_grid')
    questionary.print('\t\t\tAll entries', style='bold')
    print(table)


def show_entry_complete():
    master_password = questionary.password(
        'Enter your master password:', qmark='-').ask()
    answer = User.check_master_password(1, master_password)
    if len(answer) == 0:
        questionary.print('Invalid password', style='fg:darkred')
    else:
        id = questionary.text('Enter the entry\'s id you are looking for:',
                              validate=check_not_empty, qmark='-').ask()
        data = Password.find_entry(id)
        headers = ['URL', 'USERNAME', 'PASSWORD', 'DESCRIPTION']
        table = tabulate([data[0][2:]], headers, tablefmt='fancy_grid')
        questionary.print(f'\t\t{data[0][1]} (entry {id})', style='bold')
        print(table)


def change_entry():
    master_password = questionary.password('Enter your master password:',
                                           qmark='-').ask()
    answer = User.check_master_password(1, master_password)
    if len(answer) == 0:
        questionary.print('Invalid password', style='fg:darkred')
    else:
        id = questionary.text('Enter the id of the entry you want to modify:',
                              validate=check_not_empty, qmark='-').ask()
        first_name = questionary.text('New name:',
                                      validate=check_not_empty, qmark='-').ask()
        username = questionary.text('New username:',
                                    validate=check_not_empty, qmark='-').ask()
        password = questionary.text('New password:',
                                    validate=check_not_empty, qmark='-').ask()
        description = questionary.text('New description:', qmark='-').ask()
        url = questionary.text('New url:', qmark='-').ask()
        answer = Password.change_entry(
            id, first_name, url, username, password, description)
        print(answer)


def delete_entry():
    master_password = questionary.password(
        'Enter your master password: ', qmark='-').ask()
    answer = User.check_master_password(1, master_password)
    if len(answer) == 0:
        questionary.print('Invalid password', style='fg:darkred')
    else:
        id = questionary.text('Enter the id of the entry you want to delete:',
                              validate=check_not_empty, qmark='-').ask()
        answer = Password.delete_entry(id)
        print(answer)


if __name__ == '__main__':
    home()
