import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt

#get first index of the dataframe


df = pd.read_csv("datos/dat-ab-append.csv")

plt.plot(df["DIA_TRANSPORTE"],df["CANTIDAD"])
#move xticks slighlty to the left
plt.xticks(rotation=45, ha='right', rotation_mode='anchor', fontsize=8)
plt.show()