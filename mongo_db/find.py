# In MongoDB we use the find() and find_one() methods to find data in a collection.
# Just like the SELECT statement is used to find data in a table in a MySQL database.

# Find one

import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclint['Sai']
mycol = mydb['customers']

x = mycol.find_one()

print(x)

print('~' * 120)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# find all

import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclint['Sai']
mycol = mydb['customers']

for x in mycol.find():
    print(x)

print('~' * 120)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Return Only Some Fields

import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclint['Sai']
mycol = mydb['customers']

for x in mycol.find({},{"_id": 0, "name": 1, "address": 1}):
    print(x)

print('~' * 120)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

# without address
import pymongo

myclint = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclint['Sai']
mycol = mydb['customers']

for x in mycol.find({},{"address": 0}):
    print(x)

print('~' * 120)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Sai"]
mycol = mydb["customers"]

# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x)

for x in mycol.find({},{ "name": 1 }):
    print(x)