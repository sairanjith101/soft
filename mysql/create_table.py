import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "simple"
)

mycursor = mydb.cursor()

mycursor.execute("create table customers(id int auto_increment primary key, name varchar(255), address varchar(255))")

mycursor.execute("alter table customers add column age int not null")

mycursor.execute("show tables")

for x in mycursor:
    print(x)