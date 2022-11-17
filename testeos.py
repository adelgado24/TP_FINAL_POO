import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt

#get first index of the dataframe


df = pd.read_csv("datos/dat-ab-append.csv")

a = df["NOMBRE_EMPRESA"].value_counts(10).head(10)

#make 2 subpplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.barh(a.index, a.values)

#concat 2 df
df2 = pd.read_csv("datos/dat-ab-append.csv")
df3 = pd.concat([df, df2], axis=0)
