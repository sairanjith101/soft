import mysql.connector

# Wildcard Characters

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'gh'
)

mycursor = mydb.cursor()

sql = "select * from human where name = %s"
nam = ("Ranjith",)

mycursor.execute(sql, nam)

result = mycursor.fetchall()

for x in result:
    print(x)