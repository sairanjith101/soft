import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="gh"
)

# Create cursor object
mycursor = mydb.cursor()

# Execute SQL query
mycursor.execute("SELECT * FROM human")

# Fetch all the rows from the result set
result = mycursor.fetchall()

# Display the results
for row in result:
    print(row)

# Close cursor and connection
mycursor.close()
mydb.close()
