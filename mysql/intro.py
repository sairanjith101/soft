import mysql.connector


# Create Connection

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345'
)

print(mydb)