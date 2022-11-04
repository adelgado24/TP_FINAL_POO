import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt


# Cargamos los datos

#make 2 subplots

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
#plot 1st
ax1.plot(df['Fecha'], df['Casos'], color='red')
#add xlabel to ax1
ax1.set_xlabel('Fecha')