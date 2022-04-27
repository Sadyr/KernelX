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
for tb in mycursor:
    a = tb[0] + tb[1] + "\n"
    print(tb)
print(a)
b = 'masha' + '98765' + "\n"
print(a)
print(b)
if a == b:
    print('Yse')
else:
    print('No')
mydb.close()













# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="164.92.160.106",
#   user="sadyr",
#   password="Nimeria_1227"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)
