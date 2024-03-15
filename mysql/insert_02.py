import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="simple"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)"
val = [
  ('Peter', 'Lowstreet 4', 12),
  ('Amy', 'Apple st 652', 14),
  ('Hannah', 'Mountain 21', 15),
  ('Michael', 'Valley 345', 16),
  ('Sandy', 'Ocean blvd 2', 17),
  ('Betty', 'Green Grass 1', 18),
  ('Richard', 'Sky st 331', 19),
  ('Susan', 'One way 98', 20),
  ('Vicky', 'Yellow Garden 2', 21),
  ('Ben', 'Park Lane 38', 22),
  ('William', 'Central st 954', 23),
  ('Chuck', 'Main Road 989', 24),
  ('Viola', 'Sideway 1633', 25)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")