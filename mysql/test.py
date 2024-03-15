import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'gh'
)

mycursor = mydb.cursor()

mycursor.execute('select * from human')

result = mycursor.fetchall()

for x in result:
    print(x)