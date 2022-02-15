import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['movies']


res= mycol.aggregate([
        {
            '$unwind': {
                'path': '$genres',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$project': {
                'title': 1,
                'rating': '$imdb.rating',
                'genres': 1
            }
        }, {
            '$sort': {
                'rating': -1
            }
        }, {
            '$match': {
                'rating': {
                    '$ne': ''
                }
            }
        }, {
            '$group': {
                '_id': '$genres',
                'movies': {
                    '$push': {
                        'movie': '$title',
                        'rating': '$rating'
                    }
                }
            }
        }, {
            '$project': {
                'movies': {
                    '$slice': [
                        '$movies', 0, 10
                    ]
                }
            }
        }
])

for i in res:
    print(i)
