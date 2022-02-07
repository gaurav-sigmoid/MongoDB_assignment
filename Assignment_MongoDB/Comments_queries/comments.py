import datetime
import json
from bson import ObjectId
import pymongo
from pymongo import MongoClient
import datetime
import movies, sessions, users, theaters

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['comments']

data = []
file1 = open('comments.json', 'r')
lines = file1.readlines()
for line in lines:
    line = json.loads(line.strip())
    if '_id' in line:
        line['_id'] = ObjectId(line['_id']['$oid'])
    if 'date' in line:
        x = line['date']['$date']['$numberLong']
        datetime_obj = datetime.datetime.fromtimestamp(int(x)/1e3)
        line['date'] = datetime_obj
    if 'movie_id' in line:
        line['movie_id'] = ObjectId(line['movie_id']['$oid'])
    data.append(line)

mycol.insert_many(data)

