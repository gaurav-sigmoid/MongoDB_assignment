import json
from bson import ObjectId
import pymongo

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['theaters']

data = []
file1 = open('theaters.json', 'r')
lines = file1.readlines()
for line in lines:
    line = json.loads(line.strip())
    if '_id' in line:
        line['_id'] = ObjectId(line['_id']['$oid'])
    if 'theaterId' in line:
        if '$numberInt' in line['theaterId']:
            line['theaterId'] = int(line['theaterId']['$numberInt'])
    if 'location' in line:
        if 'geo' in line['location']:
            if 'coordinates' in line['location']['geo']:
                line['location']['geo']['coordinates'][0] = float(line['location']['geo']['coordinates'][0]['$numberDouble'])
                line['location']['geo']['coordinates'][1] = float(line['location']['geo']['coordinates'][1]['$numberDouble'])

    data.append(line)

mycol.insert_many(data)

