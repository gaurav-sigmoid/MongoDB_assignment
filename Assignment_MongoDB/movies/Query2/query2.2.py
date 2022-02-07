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
    {"$project": {"directors": "$directors", "year": "$year"}},
    {"$match": {"$and": [{"directors": {"$exists": "true", "$ne": "null"}}, {"year": 2012}]}},
    {"$group": {"_id": {"directors": "$directors"}, "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
for i in res:
    print(i)
