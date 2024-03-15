import mysql.connector

# Wildcard Characters

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'gh'
)

mycursor = mydb.cursor()

sql = "select * from human where name LIKE '%ja%'"

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)