import pandas as pl
import matplotlib.pyplot as plt

"""
Incluindo annotates
"""
dataframe = pl.read_csv('covid_19_data.csv')

df_sample = dataframe.sample(n=10)

print(dataframe.columns)

plt.figure(figsize=(8, 6))


plt.bar('Confirmed', df_sample['Confirmed'], color='blue', label='Confirmed')
plt.bar('Deaths', df_sample['Deaths'], color='red', label='Deaths')
plt.bar('Recovered', df_sample['Recovered'], color='green', label='Recovered')
plt.bar('Actives', df_sample['Confirmed'] - (df_sample['Recovered'] + df_sample['Deaths']), label='Actives')
#plt.plot(dataframe['Confirmed'], color="red")

#plt.xlabel('Confirmed, Deaths, Recovered, Actives')
plt.ylabel('Number of cases')
plt.title('Corona Virus Cases')

plt.show()