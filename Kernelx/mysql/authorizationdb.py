#username = 'svet'
#password = '1234l5'
user_db = 'user.txt'

import mysql.connector

import query as q
from mysql.connector import connect, Error


mydb = connect(
host="164.92.160.106",
user = "sadyr",
password = "Nimeria_1227",
database = 'mysql')
print(mydb)


mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM users')
# for tb in mycursor:
#     a = tb[0] + tb[1] + "\n"
#     print(tb)

def user_registration():
    print('Please provide me: ')
    username = str(input('Your username: '))
    password = str(input('Your password: '))
    repeat_password = str(input('Repeat password: '))
    if password != repeat_password:
        while password != repeat_password:
            print('Passwords not equivalent. Please repeate correctly password')
            repeat_password = str(input('repeat password'))
    u_p = username + ' ' + password + '\n'
    db_users = open('user.txt', 'a')
    db_users.write(u_p)
    db_users.close()
    print(f'Conglomerations {username}. Registrations success')
    choice = str(input('You want aut or exit? if aut enter "a", if exit enter "q"'))
    if choice.lower() == 'a':
        start_aut()
    if choice.lower() == 'q':
        exit()

def get_existing_users():
    for line in mycursor:
        # This expects each line of a file to be (name, pass) separated by white space
        a = line[0] + ' ' + line[1]
        username, password = a.split()
        print()
    yield username, password

def is_authorized(username, password):
    for user in get_existing_users():
        user_name, pass_word = user
        if username == user_name and password == pass_word:
            authorizide = True
            break
        else:
            authorizide = False
            continue
    return authorizide

def user_exists(username):
    for user in get_existing_users():
        user_name, _ = user
        if username == user_name:
            authorizide = True
            break
        else:
            authorizide = False
            continue
    return authorizide

def choice_menu():
    choice = str(input('Please choice point. If want authorized, enter "a", if want registration, enter "r". For exit enter "q"'))
    if choice.lower() == 'a':
        start_aut()
    if choice.lower() == 'r':
        user_registration()
    if choice.lower() == 'q':
        exit()

def ask_user_credentials():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password"))
    return name, password

def start_aut():
    username, password = ask_user_credentials()
    if user_exists(username):
        if is_authorized(username,password):
            print('Success aut')
        else:
            print('Incorrect password')
    else:
        print('user don"t found')

choice_menu()
