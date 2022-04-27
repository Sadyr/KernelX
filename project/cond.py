import mysql.connector
from mysql.connector import connect, Error


mydb = connect(
host="164.92.160.106",
user = "sadyr",
password = "Nimeria_1227",
database = 'mysql')
print(mydb)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM users')

def get_existing_users():
    for line in mycursor:
        # This expects each line of a file to be (name, pass) separated by white space
        a = line[0] + ' ' + line[1]
        username, password = a.split()
    yield username, password
a = 'sadyr' + '12345' + '\n'
for line in get_existing_users():
    if line ==a:
        print(line)
        break

