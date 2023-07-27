import pymongo
import pandas as pd
import json
from time import sleep

with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

username = credentials['username']
password = credentials['password']

#connection with mongodb
#client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = client['codigoPostalArgentino']
collection = db['cpa']


#dataframe transform in a list of dictionaries
data = pd.read_csv("codigosCPA.csv")
data = data.to_dict(orient='records')

#data load into mongodb by parts due to ram consumption

print('\n>>Loading by parts:')
collection.insert_many(data[0:2829239])
print('1/4 loaded')
sleep(5)
collection.insert_many(data[2829239:5658478])
print('2/4 loaded')
sleep(5)
collection.insert_many(data[5658478:8487717])
print('3/4 loaded')
sleep(5)
collection.insert_many(data[8487717:11316956])
print('4/4 loaded')
sleep(5)
print('completed')

