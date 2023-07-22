import pymongo
import pandas as pd
import json
from time import sleep

with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

username = credentials['username']
password = credentials['password']

#connection with mongodb
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")


#little etl
data = pd.read_csv("codigosCPA.csv")
print(data.shape)
data['Provincia'] = data['Provincia'].str.replace('neuquén', 'neuquen')
data = data.drop_duplicates()
print(data.shape)
sleep(3)

#data upload
db = client['codigoPostalArgentino']
for prov in data['Provincia'].unique():
    dt = data[data['Provincia'] == prov]
    collection = db[prov]
    for local in dt['Localidad'].unique():
        collection = db[prov]
        dt2 = dt[dt['Localidad'] == local][['calle_avenida', 'desde', 'hasta', 'aplica', 'cp', 'cpa']]
        collection.insert_one({'provincia': prov,
                                'localidad': local,
                                'data':dt2.to_dict('records')})
        print(f'{prov}, {local} loaded')