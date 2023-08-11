import pandas as pd
from tqdm import tqdm


#localities -----------------------------------------------------------------------
def localities_loader(data, db):
    collection = db['localities']
    data_for_localities = data.to_dict(orient="records")
    print("---> Loading localities collection")
    for item in tqdm(data_for_localities):
        collection.insert_one({
                  "id": item['id'],
                  "name": item['Localidad'],
                  "zip": item['cpa'],
                  "state": item['Provincia']})
        


#street ---------------------------------------------------------------------------
def street_loader(data_street, db):
    street_types = ["calle", "avenida", "ruta", "pasaje", "autopista"]
    collection = db['streets']
    print("---> Loading street collection")
    for stype in street_types:
        print(f"---> Loading {stype} street type")
        filtered_data = data_street[data_street['calle_avenida'].str.contains(stype)]
        filtered_data = filtered_data.to_dict(orient="records")

        for item in tqdm(filtered_data):
            collection.insert_one({
                      "id": item['street_id'],
                      "type": stype,
                      "name": item['calle_avenida'],
                      "reference": item['calle_avenida'],
                      "localityId": item['id'],
                      "neighborhood": ""})

    unknown_type = data_street[~data_street['calle_avenida'].str.contains('|'.join(street_types))]
    unknown_type = unknown_type.to_dict(orient="records")
    print("---> Loading street collection without a type")

    for item in tqdm(unknown_type):
        collection.insert_one({
                  "id": item['street_id'],
                  "type": "unknow",
                  "name": item['calle_avenida'],
                  "reference": item['calle_avenida'],
                  "localityId": item['id'],
                  "neighborhood": ""})
        


#numbers -----------------------------------------------------------------------------
def numbers_loader(data_street, db):
    collection = db['numbers']
    print("---> Loading numbers collection")
    data_street["aplica"] = data_street["aplica"].str.replace("números impares", "true")
    data_street["aplica"] = data_street["aplica"].str.replace('números pares', "false")
    data_street = data_street.to_dict(orient="records")
    for item in tqdm(data_street):
        collection.insert_one({
                  "streetId": item['street_id'],
                  "isOdd": item['aplica'],
                  "from": item['desde'],
                  "until": item['hasta'],
                  "zip": item['cpa']})