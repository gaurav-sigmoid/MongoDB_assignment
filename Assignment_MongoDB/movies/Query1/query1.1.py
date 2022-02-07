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
    {"$group": {"_id": {"title": "$title", "imdb_rating": "$imdb.rating"}}},
    {"$sort": {"_id.imdb_rating": -1}},
    {"$limit": 10}
])
for x in res:
    print(x)