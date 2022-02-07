import json
from bson import ObjectId
import pymongo
import datetime

client = pymongo.MongoClient()
mydb = client["mydatabase"]
mycol = mydb['movies']

data = []
file1 = open('movies.json', 'r')
lines = file1.readlines()
for line in lines:
    line = json.loads(line.strip())
    if '_id' in line:
        line['_id'] = ObjectId(line['_id']['$oid'])
    if 'runtime' in line:
        if '$numberInt' in line['runtime']:
            line['runtime'] = int(line['runtime']['$numberInt'])
    if 'num_mflix_comments' in line:
        if '$numberInt' in line['num_mflix_comments']:
            line['num_mflix_comments'] = int(line['num_mflix_comments']['$numberInt'])
    if 'released' in line:
        if '$date' in line['released']:
            x = line['released']['$date']['$numberLong']
            datetime_obj = datetime.datetime.fromtimestamp(int(x) / 1e3)
            line['released'] = datetime_obj
    if 'awards' in line:
        if 'wins' in line['awards']:
            if '$numberInt' in line['awards']['wins']:
                line['awards']['wins'] = int(line['awards']['wins']['$numberInt'])
        if 'nominations' in line['awards']:
            if '$numberInt' in line['awards']['nominations']:
                line['awards']['nominations'] = int(line['awards']['nominations']['$numberInt'])
    if 'lastupdated' in line:
        line['lastupdated'] = line['lastupdated']
    if 'year' in line:
        if '$numberInt' in line['year']:
            line['year'] = int(line['year']['$numberInt'])
    if 'imdb' in line:
        if 'rating' in line['imdb']:
                if '$numberDouble' in line['imdb']['rating']:
                    line['imdb']['rating'] = float(line['imdb']['rating']['$numberDouble'])
        if 'votes' in line['imdb']:
                if '$numberInt' in line['imdb']['votes']:
                    line['imdb']['votes'] = int(line['imdb']['votes']['$numberInt'])
        if 'id' in line['imdb']:
                if '$numberInt' in line['imdb']['id']:
                    line['imdb']['id'] = int(line['imdb']['id']['$numberInt'])
    if 'tomatoes' in line:
        if 'viewer' in line['tomatoes']:
            if 'rating' in line['tomatoes']['viewer']:
                    if '$numberInt' in line['tomatoes']['viewer']['rating']:
                        line['tomatoes']['viewer']['rating'] = int(line['tomatoes']['viewer']['rating']['$numberInt'])
            if 'numReviews' in line['tomatoes']['viewer']:
                if '$numberInt' in line['tomatoes']['viewer']['numReviews']:
                    line['tomatoes']['viewer']['numReviews'] = int(line['tomatoes']['viewer']['numReviews']['$numberInt'])
            if 'meter' in line['tomatoes']['viewer']:
                if '$numberInt' in line['tomatoes']['viewer']['meter']:
                    line['tomatoes']['viewer']['meter'] = int(line['tomatoes']['viewer']['meter']['$numberInt'])
        if 'lastUpdated' in line['tomatoes']:
            if '$date' in line['tomatoes']['lastUpdated']:
                x = int(line['tomatoes']['lastUpdated']['$date']['$numberLong'])
                datetime_obj = datetime.datetime.fromtimestamp(int(x) / 1e3)
                line['tomatoes']['lastUpdated'] = datetime_obj
    data.append(line)

mycol.insert_many(data)

