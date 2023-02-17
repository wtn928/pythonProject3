import mysql
import flask
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yu2000816",
    database="testdatabase2"
)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE testdatabase2")

#mycursor.execute("CREATE TABLE Person2 (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# db = mycursor.execute("DESCRIBE Person2")
# print(db)

mycursor.execute('INSERT INTO Person2 (name, age) VALUES (%s,%s)', ('Andy2', 38))
db.commit()

mycursor.execute("SELECT * FROM Person2")
for x in mycursor:
    print(x)

print('hellow world!')


