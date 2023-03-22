class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(float(self.cena_jed)*float(self.ilosc))

p1 = NaZakupy('jajka', '12', 'szt', '0.2')
p1.wyswietl_produkt()
p1.ile_produktu()
p1.ile_kosztuje()