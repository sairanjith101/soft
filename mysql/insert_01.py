import mysql.connector

# insert single row
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'simple'
)

mycursor = mydb.cursor()

sql = "insert into customers (name, address, age) values (%s, %s, %s)"
val = ("Ranjith", "Chennai", 28)

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted")