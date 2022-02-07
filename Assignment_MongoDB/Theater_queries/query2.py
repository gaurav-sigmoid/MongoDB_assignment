import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['theaters']

res = mycol.aggregate(
    [
     {
         "$geoNear":{
             "near": { "type": "Point", "coordinates": [-84.526169, 37.986019] },
             "maxDistance":10*10000000000000,
             "distanceField": "dist.calculated",
             "includeLocs": "dist.location",
             "distanceMultiplier":1/1000,
             "spherical": "true"
      }
     },
     {"$project": {"city": "$location.address.city", "distance": "$dist.calculated"}},
     {"$group": {"_id": {"distance": "$distance", "city" : "$city"} }},
     {"$sort": {"_id.distance": 1}},
     {"$limit": 10}
    ]);
for i in res:
    print(i)
