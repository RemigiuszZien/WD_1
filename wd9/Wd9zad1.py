import numpy as np
import pandas as pd

# Zad1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df)

# Zad 2
# print(df[df['Liczba']>1000])

# print(df[df['Imie']=='REMIGIUSZ'])

# print(df['Liczba'].sum())

# print(df.Liczba[(df['Rok'].isin([2000,2001,2002,2003,2004,2005]))].sum())

# print(df['Liczba'].sum())

# print(df.groupby('Plec')['Liczba'].sum())

# grouped = df.groupby(['Rok', 'Plec'])['Liczba'].max()
# for rok in df['Rok'].unique():
#     for plec in df['Plec'].unique():
#         maxv = grouped.loc[(rok, plec)]
#         maxi = df.loc[(df['Rok'] == rok) & (df['Plec'] == plec) & (df['Liczba'] == maxv), 'Imie'].values[0]
#         print(f"Rok: {rok}, Plec: {plec}, Imie: {maxi}")
#
#
# grouped2 = df.groupby('Plec')['Liczba'].max()
# for plec in df['Plec'].unique():
#     max_v = grouped2.loc[plec]
#     max_i=df.loc[(df['Plec']==plec)& (df['Liczba']==max_v),'Imie'].values[0]
#     print(f'Plec: {plec}, Name: {max_i}')

#Zad 3
df2 = pd.read_csv('zamowienia.csv',header=0, sep=';',decimal='.')
#print(df2['Sprzedawca'].unique())
#print(df2.sort_values(by='Utarg',ascending=0).head(5))