# a = 'napis'
# print(a)
# b = 5
# c = 11
# print(b, c)
# d = 5 + 3j
# print(d)
# e = c + d
# print(e)
# f = c // b
# print(f)
# g = c % b
# print(g)
# h = b ** 2
# print(h)
# i = b**1/2
# j = pow(b, 1/2)
# print(i)
# print(j)
#
# print('b = b + 2')
# print('b')
# b += 2
# print(b)
#
# listy = [1, 28, 2, 4, 16, 6, 7]
# print(listy)
#
# # dodać element na wybrane miejsce
# listy.insert(5, 2)
# print(listy)
# # dodać kilka elementów
# elementy = [20, 10, 9, 10]
# listy.extend(elementy)
# print(listy)
# # usunąć element z listy o danej pozycji
# del listy[5]
# print(listy)
# # usunąć element z listy o danej wartości
# listy.remove(2)
# print(listy)
# # odwrócić elementy listy
# listy.reverse()
# print(listy)
# # zrobić sortowanie
# listy.sort()
# print(listy)

# slownik = {'a': 2, 1: 2, 4: 'ab'}
# print(slownik[4])
# slownik['klucz'] = 'wartosc'
# print(slownik['klucz'])
# slownik.pop('klucz')
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print('a = {}, b = {}'.format(12,12))

# if warunek1:
# instrukcja1
# instrukcja2
# elif warunek2:
# instrukcja1
# instrukcja2
# else:
# instrukcja1

# a = input('podaj a: ')
# b = input('podaj b: ')
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# b = int(b)
# a = int(a)
# print(type(a))
# print(type(b))
# if a>b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print('a jest rowne b')
# if a == b:
#     print('a jest rowne b')
# else:
#     print('a nie jest rowne b')

# a = input('podaj a: ')
# b = input('podaj b: ')
# c = input('podaj c: ')
# d = input('podaj d: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print('a wieksze od b i c wieksze od d')
# else:
#     print('a < b lub c < d')

# for element in sekwencja:
    # instrukcja1
    # instrukcja2
# else:
    # instrukcja1
    # instrukcja2
# for x in range(1, 6, 1):
#     print(x)
# else:
#     print('koniec petli for')

# listy = [1, 2, 3]
# for x in listy:
#     print(x)

# listy = [1, 2, 16]
# for x in range(0, len(listy)):
#     print(listy[x])

#while warunek:
    # instrukcja1
    # instrukcja2
#else:
    # instrukcja1
    # instrukcja2

# licznik = 0
# while licznik != len(listy):
#     print(listy[licznik])
#     licznik += 1

# liczby = [1, 5, 9, 15, 20, 14, 7, 21]
# a = int(input('podaj a = '))
# licznik = 0
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#     licznik += 1
#

liczby = [1, 2, 2, 2, 4, 5, 6]
licznik = 0
while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.pop(licznik)
    else:
        licznik += 1
print('petla zakonczona', liczby)
