def czyProstokatny(a, b, c):
    if (a >= b and a >= c):
        najwiekszy=a
    elif (b >= a and b >= c):
        najwiekszy = b
    else:
        najwiekszy = c
    suma = (a**2 + b**2 + c**2) - najwiekszy**2
    if suma == najwiekszy**2:
        return 'trojkat jest prostokatny'
    else:
        return 'trojkat nie jest prostokatny'

a=3
b=4
c=5
x = czyProstokatny(a,b,c)
print (x)
