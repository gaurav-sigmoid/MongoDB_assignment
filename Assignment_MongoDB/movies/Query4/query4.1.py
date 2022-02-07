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
    {"$unwind": "$genres"},
    {"$project": {"rating": "$imdb.rating","genres": "$genres", "title": "$title"}},
    {"$group": {"_id": {"genres": "$genres", "max_rating": {"$max": "$rating"}, "title": {"first": "$title"}}}},
    {"$sort": {"_id.max_rating": -1}},
    {"$limit": 10}
])
for i in res:
    print(i)
