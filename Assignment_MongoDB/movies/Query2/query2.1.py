import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['movies']

res = mycol.aggregate([
    {"$project": {"directors": "$directors"}},
    {"$match": {"directors": {"$exists": "true", "$ne": "null"}}},
    {"$group": {"_id": {"directors": "$directors"}, "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
for x in res:
    print(x)