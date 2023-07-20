import pymongo
import pandas as pd
import json


with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

username = credentials['username']
password = credentials['password']

#connection with mongodb
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")

db = client['codigoPostalArgentino']
collection = db['cpa']


#dataframe transform in a list of dictionaries
data = pd.read_csv("codigosCPA.csv")
data = data.to_dict(orient='records')

#data load into mongodb by parts due to ram consumption
collection.insert_many(data[0:2829239])

collection.insert_many(data[2829239:5658478])

collection.insert_many(data[5658478:8487717])

collection.insert_many(data[8487717:11316956])


