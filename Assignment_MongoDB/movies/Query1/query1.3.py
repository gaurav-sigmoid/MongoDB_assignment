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
    {"$project": {"votes": "$imdb.votes", "rating": "$imdb.rating", "title": "$title"}},
    {"$match": {"votes": {"$gt": 1000}}},
    {"$group": {"_id": {"title": "$title", "rating": "$rating", "votes": "$votes"}}},
    {"$sort": {"_id.rating": -1, "_id.votes": -1}},
    {"$limit": 10}
])
for x in res:
    print(x)