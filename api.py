from fastapi import FastAPI
import pymongo
import json

#pymongo connection
with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

username = credentials['username']
password = credentials['password']

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster-palta-cpa.nyymbgr.mongodb.net/")
#client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['codigoPostalArgentino']

#fastAPI instance
app = FastAPI()


#returns a list of dictionaries containing data from all "calle_avenida" in a province, locality
@app.get("/{provincia}/{localidad}")
def cpa_localidad_lista(provincia:str, localidad:str):
    x = db[provincia].find_one({'localidad':localidad})
    return list(x['data'])

#returns a dictionary containing the data of an specific file
@app.get("/{provincia}/{localidad}/{calle_avenida}/{desde}")
def cpa_especifico(provincia:str, localidad:str, calle_avenida:str, desde:int):
    x = db[provincia].find_one({"$and": [
        {"localidad": localidad},
        {"data": {
                "$elemMatch": {
                    "calle_avenida": calle_avenida,
                    "desde": desde }}}]}, 
                    {"data.$": 1})
    return x['data'][0]

#returns a dictionary containing data give a certain "cpa"
@app.get("/{cpa}")
def data_cpa(cpa:str):
    for prov in db.list_collection_names():
        x = db['tucuman'].find_one({"data": {
                "$elemMatch": {"cpa":"T4174ADA"}}}, {'data.$':1})
    return x['data'][0]

