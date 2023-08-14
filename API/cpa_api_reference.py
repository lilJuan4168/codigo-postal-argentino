from fastapi import FastAPI
import pymongo
import json
from bson.json_util import dumps, loads
#pymongo connection
with open('credentials.json', 'r') as cred:
    credentials = json.load(cred)

uri = credentials['uri']
 
client = pymongo.MongoClient(uri)
db = client['codigoPostalArgentino_v3']

#fastAPI instance
app = FastAPI()

#returns a list of dictionaries containing data from all "calle_avenida" in a province, locality
@app.get("/{provincia}/{localidad}")
async def cpa_localidad(provincia:str, localidad:str):
          x = dumps(db["localities"].find({
            "state": provincia, "name": localidad}, 
           {
             "name":1,"state":1,"zip":1, "id":1, "_id":0}
            ))
          return json.loads(x)


@app.get("/{provincia}/{localidad}/{calle_avenida}/{desde}/{hasta}")
async def cpa_especifico(provincia:str, localidad:str, calle_avenida:str, desde:int, hasta:int): 
          x = dumps(db['streets'].aggregate([
                  {"$match":{"name": calle_avenida}},
                  {"$lookup":{
                          "from": "localities",
                          "localField": "localityId",
                          "foreignField": "id",
                          "as": "locality_data"
                  }},
                  {"$unwind": "$locality_data"},
                  {"$lookup":{
                          "from":"numbers",
                          "localField":"id",
                          "foreignField":"streetId",
                          "as":"numbers_data"
                  }},
                  {"$unwind": "$numbers_data"},
                  {"$match":{"numbers_data.from":desde, 
                             "numbers_data.until":hasta,
                             "locality_data.name": localidad, 
                             "locality_data.state":provincia}},
                  {"$project":{
                          "_id":0,
                          "name":1,
                          "type":1,
                          "locality_data.name":1,
                          "locality_data.state":1,
                          "numbers_data.zip":1
                  }}
          ]))

          return json.loads(x)
 

@app.get("/{cpa}")
async def data_cpa(cpa:str):
          x = dumps(db['numbers'].aggregate([
                 {"$match": {"zip": cpa}},
                 {"$lookup": {
                        "from": "streets",
                        "localField": "streetId",
                        "foreignField": "id",
                        "as": "streets_data"
                 }},
                 {"$unwind": "$streets_data"},
                 {"$lookup":{
                        "from": "localities",
                        "localField": "streets_data.localityId",
                        "foreignField": "id",
                        "as": "locality_data"
                 }},
                 {"$unwind": "$locality_data"},
                 {"$project":{"_id":0, 
                              "streets_data.name":1, 
                              "from":1, 
                              "until":1, 
                              "zip":1,
                              "locality_data.name":1, 
                              "locality_data.state":1 }}
          ]))

          return json.loads(x)





