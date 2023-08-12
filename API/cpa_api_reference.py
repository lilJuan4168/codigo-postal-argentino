from fastapi import FastAPI
import pymongo
import json
from bson.json_util import dumps, loads
#pymongo connection
with open('../credentials.json', 'r') as cred:
    credentials = json.load(cred)

uri = credentials['uri']
 
client = pymongo.MongoClient(uri)
#client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['codigoPostalArgentino_v3']

#fastAPI instance
app = FastAPI()

#returns a list of dictionaries containing data from all "calle_avenida" in a province, locality
@app.get("/{provincia}/{localidad}")
def cpa_localidad(provincia:str, localidad:str):
    x = dumps(db["localities"].find({"state": provincia, "name": localidad}, {"name":1,"state":1,"zip":1}))
    return json.loads(x)
    