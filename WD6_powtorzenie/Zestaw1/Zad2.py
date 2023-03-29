def funkcja(lista1,lista2):
    lista3 = []
    while len(lista1) > len(lista2):
        lista2.append(0)

    while len(lista2) > len(lista1):
        lista1.append(0)

    for i in range(0, len(lista1)):
        lista3.append(lista1[i]+lista2[i])

    return lista3

x=[1,2,3,4,5]
z=[1,2,3,4,5,6,7]
print(funkcja(x,z))