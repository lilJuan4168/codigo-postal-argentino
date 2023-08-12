import pymongo
import pandas as pd
import json
from functions.reference_functions import *

with open('../credentials.json', 'r') as cred:
    credentials = json.load(cred)

uri = credentials['uri']


#connection with mongodb -------------------------------------------

client = pymongo.MongoClient(uri)
print("---> Mongo client connected")

#create database connection
db = client['codigoPostalArgentino_v3']

#load main datafile
data = pd.read_csv("../data/CPA_data_converted.csv")
print("---> CSV load completed")

#localities ---------------------------------------------------------                  
localities_loader(data, db)

#data filtering for streets
data = data[~data["calle_avenida"].isnull()]
data['street_id'] = range(len(data))

#streets ---------------------------------------------------------
street_loader(data, db)

#numbers ---------------------------------------------------------
numbers_loader(data, db)

print("---> Load completed")


