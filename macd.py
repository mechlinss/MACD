import pandas as pd

extracted_data = pd.read_csv("data/eth_v_d.csv")

print(extracted_data.head())

date = extracted_data[["Data"]]
open = extracted_data[["Otwarcie"]]

print(date.head())