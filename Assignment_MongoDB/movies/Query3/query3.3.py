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
    {"$unwind": "$cast"},
    {"$project": {"actor": "$cast", "year": "$year", "genres": "$genres"}},
    {"$match": {"$and": [{"actor": {"$exists": "true", "$ne": "null"}}, {"genres": {"$in": ["Short"]}}]}},
    {"$group": {"_id": {"actor": "$actor"}, "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
for i in res:
    print(i)
