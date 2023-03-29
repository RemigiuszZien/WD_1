try:
    a = int(input("Podaj liczbe calkowita a: "))
    b = int(input("Podaj liczbe calkowita b: "))
    wynik = a**2 + a*b + b**2
    with open ('zadanie1.txt', 'w') as f:
        f.write(str(wynik))
        print("Wynik zostal zapisany")
except ValueError:
    print(f"Wprowadzono nieprawidlowe dane")