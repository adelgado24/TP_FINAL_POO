import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt

#make df with date column

df = pd.DataFrame({'date': pd.date_range('2018-01-01', periods=10, freq='D')})
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

#Add a date row



#plt x axis title



