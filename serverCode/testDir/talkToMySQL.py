#! /usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jamie",
  passwd="#Ga1!axy"
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)
