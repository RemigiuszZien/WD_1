def funkcja(lista1):

    for i in range(0, len(lista1)):
        lista1.append(lista1[0]+lista1[i])
    return lista1
x= [1,2,3,4,5,6,7]
print(x)
print(funkcja(x))