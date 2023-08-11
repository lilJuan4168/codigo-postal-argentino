import pymongo
import pandas as pd
import json


with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

username = credentials['username']
password = credentials['password']

#connection with mongodb
#client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

data = pd.read_csv("../data/CPA_data_converted.csv")

db = client['codigoPostalArgentino']

collection = db['localities']
collection.insert_one({
    "id": data['id'],
    "name": data['Localidad'],
    "zip": data['cpa'],
    "sate": data['Provincia']
})

collection = db['streets']
collection.insert_one()