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
data = pd.read_csv("../data/CPA_data_converted.csv")
data = data.to_dict(orient='records')

x = len(data) // 2
#data load into mongodb by parts due to ram consumption

print('\n>>Loading by parts:')
collection.insert_many(data[0:x])
print('1/2 loaded')
sleep(5)
collection.insert_many(data[x:2*x])
print('2/2 loaded')
sleep(5)

print('completed')

