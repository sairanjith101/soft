# A collection in MongoDB is the same as a table in SQL databases.
# Important: In MongoDB, a collection is not created until it gets content!


import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclint['Sai']

mycol = mydb["customers"]

# Inserting some data into the "check" collection
mycol.insert_one({"example": "data"})

print(myclint.list_database_names())

dblist = myclint.list_database_names()

if "Sai" in dblist:
    print(" The database exists in the database")
else:
    print(" The database does not exist")


