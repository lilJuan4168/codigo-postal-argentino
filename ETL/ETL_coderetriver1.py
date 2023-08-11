import pandas as pd

coderetriver1 = pd.read_csv("../data/coderetriver1_data.csv")

#to lowercase
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.lower()
coderetriver1['Localidad'] = coderetriver1['Localidad'].str.lower()
coderetriver1['calle_avenida'] = coderetriver1['calle_avenida'].str.lower()

#replace words and drop duplicates
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('entre ríos', 'entre rios')
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('tucumán', 'tucuman')
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('córdoba', 'cordoba')
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('río negro', 'rio negro')
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('santa fé', 'santa fe')
coderetriver1['Provincia'] = coderetriver1['Provincia'].str.replace('neuquén', 'neuquen')

#drop duplicates
coderetriver1 = coderetriver1.drop_duplicates()

#data cleaning
provincias = ['buenos aires', 'capital federal', 'catamarca', 'chaco', 'chubut', 'cordoba', 
              'corrientes', 'entre rios', 'formosa', 'jujuy', 'la pampa', 'la rioja', 
              'mendoza', 'misiones', 'neuquen', 'rio negro', 'salta', 'san juan', 'san luis', 
              'santa cruz', 'santa fe', 'santiago del estero', 'tierra del fuego', 'tucuman']

good_data = coderetriver1[coderetriver1['Provincia'].isin(provincias)].sort_values(by='Provincia')

good_data['desde'] = good_data['desde'].astype('Int64')
good_data['hasta'] = good_data['hasta'].astype('Int64')

#reset index
good_data = good_data.reset_index(drop=True)

#save good data
good_data.to_csv("../data/good_data1.csv", index=False)

#filter bad data

bad_data = coderetriver1[~coderetriver1['Provincia'].isin(provincias)].sort_values(by='Provincia')


bad_data['Localidad'] = bad_data['Localidad'].str.replace('entre ríos', 'entre rios')
bad_data['Localidad'] = bad_data['Localidad'].str.replace('tucumán', 'tucuman')
bad_data['Localidad'] = bad_data['Localidad'].str.replace('córdoba', 'cordoba')
bad_data['Localidad'] = bad_data['Localidad'].str.replace('río negro', 'rio negro')
bad_data['Localidad'] = bad_data['Localidad'].str.replace('santa fé', 'santa fe')
bad_data['Localidad'] = bad_data['Localidad'].str.replace('neuquén', 'neuquen')

#save bad data
bad_data.to_csv("../data/bad_data.csv", index=False)