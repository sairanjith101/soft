# A document in MongoDB is the same as a record in SQL databases.

import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclint['Sai']

mycol = mydb["customers"]

# Insert Into Collection
mydict = {'name': 'siva', 'age': 29}

x = mycol.insert_one(mydict)

print(x)

# Return the _id Field
print(x.inserted_id)

# Insert Many

mylist = [
    {'name': 'a', 'age': 1},
    {'name': 'b', 'age': 2},
    {'name': 'c', 'age': 3},
    {'name': 'd', 'age': 4},
    {'name': 'e', 'age': 5}
]

y = mycol.insert_many(mylist)

print(y)
print(y.inserted_ids)

# Insert Multiple Documents, with Specified IDs
uniq = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

z = mycol.insert_many(uniq)
print(z.inserted_ids)