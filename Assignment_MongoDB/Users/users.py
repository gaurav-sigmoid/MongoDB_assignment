import json
from bson import ObjectId
import pymongo

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['users']

data = []
file1 = open('users.json', 'r')
lines = file1.readlines()
for line in lines:
    line = json.loads(line.strip())
    if '_id' in line:
        line['_id'] = ObjectId(line['_id']['$oid'])
    data.append(line)

mycol.insert_many(data)

