import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# zad1
x1 = np.arange(1, 20.0001, 0.1)
plt.plot(x1, 1 / x1, label="1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.axis([1, 20, 0, 1])
#plt.show()

# Zad2
x2 = np.arange(1, 20, 1)
plt.plot(x2, 1 / x2, 'g:>', label='f(x) = 1/x' )
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.axis([1, 20, 0, 1])
#plt.show()

# Zad3
x3 = np.arange(0,30.01,0.1)
plt.plot(x3,np.cos(x3),'g-',x3,np.sin(x3),'r-')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(labels=['cos(x)','sin(x)'])
#plt.show()

# Zad4
data = pd.read_csv("iris.data")
df=pd.DataFrame(data)
print(df)