import random
lista1 = []
for i in range(9):
    n = random.randint(0,500)
    lista1.append(n)
print(lista1)
lista2 = [x for x in lista1 if x%2==0]
print(lista2)