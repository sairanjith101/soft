# Creating a Database
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345'
)

mycursor = mydb.cursor()

# showing the database
mycursor.execute('show databases')

for x in mycursor:
    print(x)


# if you want run this script comment the below condent

# accessing the database

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "simple"
)
