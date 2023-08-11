import pandas as pd

code1 = pd.read_csv("../data/good_data1.csv")
code2 = pd.read_csv("../data/good_data2.csv")

print(code1.shape)
print(code2.shape)

result = pd.concat([code1, code2])

print(result.shape)

result = result.drop(["id"], axis=1)
result = result.sort_values(by='Provincia')
result = result.reset_index(drop=True)

result.to_csv("../data/cpa_data.csv", index_label="id")
