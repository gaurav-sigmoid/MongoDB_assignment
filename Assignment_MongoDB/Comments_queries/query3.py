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
    {"$project": {"month": {"$month": "$date"}, "year": {"$year": "$date"}}},
    {"$match": {"year": 2012}},
    {"$group": {"_id": {"month": "$month"}, "count": {"$sum": 1}}},
    {"$sort": {"_id.month": 1}}
])
for i in res:
    print(i)
