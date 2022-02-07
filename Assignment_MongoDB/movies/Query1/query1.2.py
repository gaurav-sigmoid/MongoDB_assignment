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
    {"$project": {"year": {"$year": "$released"}, "rating": "$imdb.rating", "title": "$title"}},
    {"$match": {"year": 2014}},
    {"$group": {"_id": {"title": "$title", "rating": "$rating"}}},
    {"$sort": {"_id.rating": -1}},
    {"$limit": 10}
])
for x in res:
    print(x)