import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('D:\Documents\Python_sheet\day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.scatter(bike_sharing['windspeed'], bike_sharing['cnt'])
plt.ylabel('Bikes Rented')
plt.xlabel('Wind Speed')
plt.show()
