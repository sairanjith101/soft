# Filter the Result

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Sai"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# Advanced Query
myquery = { "address": { "$gt": "k" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# Filter With Regular Expressions
# Regular expressions can only be used to query strings.

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)