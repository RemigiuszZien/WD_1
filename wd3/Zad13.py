lista = []
licznik = 0
while licznik<10:
    a = int(input('podaj liczbe:'))
    if a%2 == 0:
        lista.append(a)
    licznik+=1
print(lista)