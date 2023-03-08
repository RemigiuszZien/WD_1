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
listy = [1, 28, 2, 4, 16, 6, 7]
print(listy)

# dodać element na wybrane miejsce
listy.insert(5, 2)
print(listy)
# dodać kilka elementów
elementy = [20, 10, 9, 10]
listy.extend(elementy)
print(listy)
# usunąć element z listy o danej pozycji
del listy[5]
print(listy)
# usunąć element z listy o danej wartości
listy.remove(2)
print(listy)
# odwrócić elementy listy
listy.reverse()
print(listy)
# zrobić sortowanie
listy.sort()
print(listy)
