import pandas as pl
import matplotlib.pyplot as plt

"""
Incluindo annotates
"""
dataframe = pl.read_csv('coreia_sul.csv')

df_sample = dataframe.sample(n=10)

print(dataframe.columns)

plt.figure(figsize=(8, 6))

plt.plot(dataframe['ObservationDate'],(dataframe['Confirmed'] - (dataframe['Recovered'] + dataframe['Deaths'])), color="purple", label='actives')
#plt.plot(dataframe['Confirmed'], color="red")

#plt.xlabel('Confirmed, Deaths, Recovered, Actives')
plt.ylabel('Number of cases')
plt.title('Corona Virus Cases')

plt.show()