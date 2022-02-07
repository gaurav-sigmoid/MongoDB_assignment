import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['theaters']

res = mycol.aggregate([
    {"$project": {"city": "$location.address.city","theater": "$theaterId"}},
    {"$group": {"_id": {"city": "$city", "theater": "$theater"}, "num": {"$sum": 1}}},
    {"$group": {"_id": "$_id.city", "theaterCount": {"$push": {"theaterName": "$_id.theater", "count": "$num"}}}},
    {"$project": {"_id": 1, "totalTheatersAtCity": { "$sum": "$theaterCount.count"}}},
    {"$sort": {"totalTheatersAtCity": -1}},
    {"$limit": 10}
])
for i in res:
    print(i)
