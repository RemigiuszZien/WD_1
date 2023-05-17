import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(rc={'figure.figsize':(8,8)})
# sns.lineplot(x=[1, 2, 3, 4], y = [1, 4, 9, 16], label='linia nr',
#              color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y = [2, 5, 10, 17], label='x^2+1',
#              color='red', marker='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('wykres liniowy')
# plt.show()
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii')
# wykres.fig.set_size_inches(8,6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartosci')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()
data = pd.read_csv('iris.data',header=0,sep=',',decimal='.')
df = pd.DataFrame(data)
sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow','green','blue'])
plt.xlabel("index")
plt.ylabel("sepal length")
plt.show()