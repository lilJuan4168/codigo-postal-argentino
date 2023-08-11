import pandas as pd

data1 = pd.read_parquet('../data/CPA_DATA.parquet')


data1.to_csv('../data/CPA_data_converted.csv', index=False)