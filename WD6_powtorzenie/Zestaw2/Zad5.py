try:
    n = int(input("Podaj nieujemna liczbe calkowita n: "))
    wynik = 0
    for i in range(0,n+1):
        wynik+=i

    with open ('zadanie5.txt', 'w') as f:
        f.write(str(wynik))
        print("Wynik zostal zapisany")
except ValueError:
        print("Podano nieprawidlowe dane")

