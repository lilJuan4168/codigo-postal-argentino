from fastapi import FastAPI
import pymongo
import json

#pymongo connection
with open('../credentials.json', 'r') as cred:
    credentials = json.load(cred)

uri = credentials['uri']

client = pymongo.MongoClient(uri)

db = client['codigoPostalArgentino']

#fastAPI instance
app = FastAPI()

#returns a list of dictionaries containing data from all "calle_avenida" in a province, locality
@app.get("/{provincia}/{localidad}")
def cpa_localidad_lista(provincia:str, localidad:str):
    x = db[provincia].find_one({'localidad':localidad})
    if x is None:
        return "not found"
    else:
       return list(x['data'])

#returns a list of dictionaries containing the data of an specific file or a list
@app.get("/{provincia}/{localidad}/{calle_avenida}/{desde}/{hasta}")
def cpa_especifico(provincia:str, localidad:str, calle_avenida:str, desde:int, hasta:int):
 
    x = db[provincia].find_one({"$and": [
        {"localidad": localidad},
        {"data": {
                "$elemMatch": {
                    "calle_avenida": calle_avenida,
                    "desde": desde,
                    "hasta": hasta}}}]}, 
                    {"data.$": 1})
    if x is None:
       return "not found"
    else:
       return x['data']

#returns a dictionary containing data give a certain "cpa"
@app.get("/{cpa}")
def data_cpa(cpa:str):
    for prov in db.list_collection_names():
        x = db['tucuman'].find_one({"data": {
                "$elemMatch": {"cpa":cpa}}}, {'data.$':1})
    if x is None:
        return "not found"
    else:
        return x['data'][0]
        

