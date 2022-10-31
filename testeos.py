import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt

df = pd.read_csv("datos/dat-ab-append.csv")

#groupby tipo transporte

gr = df.groupby("TIPO_TRANSPORTE")

definitvo = gr["CANTIDAD"].agg({"count","sum","mean"}).reset_index()

#make 3 subpie charts of definitivo, with matplotlib

fig, ax = plt.subplots(1,3,figsize=(15,5))

ax[0].pie(definitvo["count"],labels=definitvo["TIPO_TRANSPORTE"],autopct="%1.1f%%")
ax[0].set_title("Cantidad de viajes por tipo de transporte")
ax[1].pie(definitvo["sum"],labels=definitvo["TIPO_TRANSPORTE"],autopct="%1.1f%%")
ax[1].set_title("Cantidad de pasajeros por tipo de transporte")
ax[2].pie(definitvo["mean"],labels=definitvo["TIPO_TRANSPORTE"],autopct="%1.1f%%")
ax[2].set_title("Cantidad promedio de pasajeros por tipo de transporte")
#add percentage to pie charts
ax[0].axis("equal")
ax[1].axis("equal")
plt.show()