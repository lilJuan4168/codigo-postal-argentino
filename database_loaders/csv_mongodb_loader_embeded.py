import pymongo
import pandas as pd
import json


with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

uri = credentials['uri']


#connection with mongodb
#client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")
client = pymongo.MongoClient(uri)

#data load
data = pd.read_csv("../data/CPA_data_converted.csv")

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

