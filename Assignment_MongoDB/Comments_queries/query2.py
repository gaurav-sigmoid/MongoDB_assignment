import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['comments']

res = mycol.aggregate([
    {"$match": {}},
    {"$group": {"_id": "$movie_id", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$project":  {"sum": {"$toInt": "$count"}}},
    {"$limit": 10}
])
for i in res:
    print(i)
