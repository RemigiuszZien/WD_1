import numpy as np
import math

a = np.arange(4, 4 * 20 + 1, 4)  # Zad 1

# Zad 2
lista = [1.5, 2.3, 4.7, 3.6, 6.7]
b = np.array(lista)
print(b)
c = b.astype(dtype='int32')
print(c)
d = np.array(lista, dtype='int32')


# Zad 3
def tablica(n):
    e = np.zeros((n * n), dtype='int32')
    for i in range(0, len(e)):
        e[i] = 2 ** i
    tab = e.reshape((n, n))
    return tab


# Zad 4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

#Zad 5
def diagonalna(n):
    l = np.arange(n, -1, -1)
    diag = np.diag(l, 2)
    return diag

#Zrobic zad od 6 do 9 w domu do przerobienia
#Zad 6
# malina =
# mrowka =
# armata =
# armata = np.flip(armata)

#Zad 7
def macierz(n):
    mac = np.zeros((n,n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i)for _ in range(n-i)], k=1)
        mac += np.diag([2+(2*i)for _ in range(n-i)], k=1)
    print(mac)


