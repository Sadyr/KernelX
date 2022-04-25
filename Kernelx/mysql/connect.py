import mysql.connector

mydb = mysql.connector.connect(
  host="164.92.160.106",
  user="sadyr",
  password="Nimeria_1227"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
