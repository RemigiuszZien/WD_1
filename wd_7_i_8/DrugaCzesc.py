import numpy as np
# Zad 1
# f = np.array([1,2,3])
# e = np.array([4,5,6])
# c = e*f
# print(c)

#Zad 2
# e = np.arange(1,10).reshape((3,3))
# f = np.arange(1,17).reshape((4,4))
# print(e.min(axis=0))
# print(e.min(axis=1))
# print(f.min(axis=0))
# print(f.min(axis=1))


# Zad 3
# e = np.array([1,2,3])
# f = np.array([4,5,6])
# c = np.dot(e,f)
# print(c)


#Zad 4
# e = np.array([1,2,3])
# f = np.array([4.5,5.7,6.8])
# c = e*f
# print(c)

#Zad 5
c = np.arange(1,7).reshape((2,3))
a = np.sin(c)
print(a)

#Zad 6
d = np.arange(1,7).reshape((2,3))
b = np.cos(d)
print(b)

#Zad 7
l = a+b
print(a+b)

#Zad 8
j = np.arange(1,10).reshape((3,3))
for i in j:
    print(i)

#Zad 9
o = np.arange(1,10).reshape((3,3))
for i in o.flat:
    print(i)

#Zad 10
m = np.ones((9,9))
print(m)
print(m.reshape(3,27))
print(m.reshape(27,3))
print(m.reshape(81,1))
print(m.reshape(1,81))
#dziala bo i*j = 81

#Zad 11
v = np.arange(12)
vv = v.reshape(3,4)
vvv = v.reshape(4,3)
vvvv = v.reshape(2,6)
print(v)
print(vv.ravel())
print(vvv.ravel())
print(vvvv.ravel())