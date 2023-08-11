import pandas as pd

data = pd.read_csv("../data/cpa_data.csv")

data.to_parquet("../data/CPA_DATA.parquet")