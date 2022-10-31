import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt


# Cargamos los datos

df = {'fecha': ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05'], 'casos': [313754198, 306069353, 222294728, 59187842, 77753791]}
df = pd.DataFrame(df)

#Loc min value index

min_value = df['casos'].min()
min_index = df['casos'].idxmin()

print(min_value, min_index)
