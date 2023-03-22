class ciagi:
    def __init__(self):
        self.elementy = []
    def wyswietl_dane(self):
        print(self.elementy)

    def pobierz_elementy(self):
        self.ilosc = int(input("Podaj ilosc elementow: "))
        for i in range(0, self.ilosc):
            ele = float(input())
            self.elementy.append(ele)

    def pobierz_parametry(self):
        self.pierwsza_wartosc = float(input("Podaj a1"))
        self.roznica = float(input("Podaj roznice"))
        self.ilosc = int(input("Podaj ilosc elementow ciagu do wygenerowania"))

    def policz_sume(self):
        print(sum(self.elementy))

    def policz_elemnty(self):
       for i in range(self.ilosc):
           self.elementy.append(self.pierwsza_wartosc+i*self.roznica)



p1 = ciagi()
p1.pobierz_parametry()
p1.wyswietl_dane()
p1.policz_elemnty()
p1.wyswietl_dane()
gfdg