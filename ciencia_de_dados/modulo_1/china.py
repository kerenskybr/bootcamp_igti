import pandas as pl
import matplotlib.pyplot as plt

"""
Incluindo annotates
"""
dataframe = pl.read_csv('china.csv')

df_sample = dataframe.sample(n=10)

print(dataframe.columns)

plt.figure(figsize=(8, 6))


plt.plot(dataframe['ObservationDate'], (dataframe['Deaths']), color="yellow", label='deaths')
plt.plot(dataframe['ObservationDate'], (dataframe['Confirmed']), color="blue", label='confirmed')
plt.plot(dataframe['ObservationDate'], (dataframe['Recovered']), color="red", label='recovered')
plt.plot(dataframe['ObservationDate'], (dataframe['Confirmed'] - (dataframe['Recovered'] + dataframe['Deaths'])), color="purple", label='actives')
#plt.plot(dataframe['Confirmed'], color="red")

#plt.xlabel('Confirmed, Deaths, Recovered, Actives')
plt.ylabel('Number of cases')
plt.title('Corona Virus Cases')

plt.show()