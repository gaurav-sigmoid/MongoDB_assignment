import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime
import re

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['movies']

regx = re.compile("^b", re.IGNORECASE)
res = mycol.aggregate([
    {"$project": {"title": "$title", "rating": "$tomatoes.viewer.rating"}},
    {"$match": {"title": regx}},
    {"$group": {"_id": {"rating": "$rating", "title": "$title" }}},
    {"$sort": {"_id.rating": -1}},
    {"$limit": 10}
])
for x in res:
    print(x)