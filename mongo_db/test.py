import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Ran"]

mycol = mydb["check"]

# Inserting some data into the "check" collection
mycol.insert_one({"example": "data"})

print(myclient.list_database_names())

dblist = myclient.list_database_names()

if 'Ran' in dblist:
    print("The database is exists")
else:
    print("the database is not exists")

