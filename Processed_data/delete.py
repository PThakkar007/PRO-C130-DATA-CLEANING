import pandas as pd
import csv

df = pd.read_csv("final_data.csv")

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
print(df.shape)
axis = 'column'
df.to_csv('final_data.csv')