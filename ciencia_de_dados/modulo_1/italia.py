import pandas as pl
import matplotlib.pyplot as plt

"""
Incluindo annotates
"""
dataframe = pl.read_csv('italia.csv')

df_sample = dataframe.sample(n=10)

print(dataframe.columns)

plt.figure(figsize=(8, 6))

actives = (dataframe['Confirmed'] - (dataframe['Recovered'] + dataframe['Deaths']))
actives_mean = (dataframe['Confirmed'] - (dataframe['Recovered'] + dataframe['Deaths'])) / len(dataframe)


#plt.plot(dataframe['ObservationDate'], (dataframe['Deaths']), color="yellow", label='deaths')
#plt.plot(dataframe['ObservationDate'],(dataframe['Confirmed']), color="blue", label='confirmed')
#plt.plot(dataframe['ObservationDate'],(dataframe['Recovered']), color="red", label='recovered')
#plt.plot(dataframe['ObservationDate'],actives, color="purple", label='actives')

plt.plot(dataframe['ObservationDate'],actives, color="purple", label='actives')


plt.ylabel('Number of cases')
plt.title('Corona Virus Cases')

plt.show()