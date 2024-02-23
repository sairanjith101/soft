
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Sai"]
mycol = mydb["customers"]

# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x)

for x in mycol.find({},{ "name": 1 }):
    print(x)