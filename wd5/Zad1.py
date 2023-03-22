import random

lista1 = []
for i in range(29):
    n = random.randint(0, 30)
    lista1.append(n * 2)
plik = open("pli.txt", "w+")
plik.writelines((str(lista1)))

