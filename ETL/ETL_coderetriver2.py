import pandas as pd

coderetriver2 = pd.read_csv("../data/coderetriver2_data.csv")

#to lowercase
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.lower()
coderetriver2['Localidad'] = coderetriver2['Localidad'].str.lower()
#coderetriver2['calle_avenida'] = coderetriver2['calle_avenida'].str.lower()

#replace words and drop duplicates
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('entre ríos', 'entre rios')
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('tucumán', 'tucuman')
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('córdoba', 'cordoba')
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('río negro', 'rio negro')
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('santa fé', 'santa fe')
coderetriver2['Provincia'] = coderetriver2['Provincia'].str.replace('neuquén', 'neuquen')

#drop duplicates
coderetriver2 = coderetriver2.drop_duplicates()
coderetriver2 = coderetriver2.reset_index(drop=True)

coderetriver2.to_csv("../data/good_data2.csv", index=False)