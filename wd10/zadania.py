import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# y = np.arange(4)
# plt.plot(y)
# plt.ylabel('liczby')
# plt.show()
# x = np.array([1,2,3,4])
# y = x**2
# plt.plot(x,y,'r')
# plt.plot(x,y,'o')
# plt.axis([0,6,0,20])
# plt.show()
a = np.arange(0, 5, 0.2)
# plt.plot(a,a,'r--',a,a**2,'bs',a,a**3,'g^')
# plt.legend(labels=['liniowa','kwadratowa','szescienna'], loc='center left')
# plt.show()
# plt.plot(a,a,'r--',label='liniowa')
# plt.plot(a,a**2,'bs',label='kwadratowa')
# plt.plot(a,a**3,'g^',label='szescienna')
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title('plt title')
# plt.legend(loc='center left')
# plt.savefig('wykres1.jpg')
# plt.show()
# wykres liniowy sinusa na przedziale dla x 0,10 z krokiem 0.1
# x = np.arange(0,10.000000000001,0.1)
# y = np.sin(x)
# plt.plot(x,y,'r-')
# plt.xlabel('x')
# plt.ylabel('sin x')
# plt.title('sin x w przedziale <0,10>')
# plt.legend()
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0,50,50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 *np.random.randn(50)
# data['d'] = np.abs(data['d'])*100
# plt.scatter('a','b',c='c',s='d',data=data,cmap='winter')
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()

x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
# plt.subplot(4, 1, 1)
# plt.plot(x1,y1)
# plt.title('wykress sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2,y2,'r')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()
# fig, axs = plt.subplots(3,2)
# axs[0,0].plot(x1,y1,'g-')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('Wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'y-')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('Wykres cos(x)')
#
# axs[2,0].plot(x1,y1,'m-')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].set_title('Wykres sin(x)')
#
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
# plt.bar(etykiety, wartosc, color=['yellow', 'green', 'red'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja')
# plt.show()

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()
# df = pd.read_csv('dance.csv',header=0,sep=';',decimal='.')
# grupa = df.groupby('Imię i nazwisko').agg('{Wartość zamówienia':['sum']})
# grupa.plot(kind='pie',subplots=True,autopct='%.2f%%',fontsize=20,colors=['red','blue'])