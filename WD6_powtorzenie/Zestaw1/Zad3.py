with open('tekst.txt','r',encoding='utf-8') as plik:
    znaki = plik.read()[100:135]

licznik = 0
for znak in znaki:
    if znak.isupper():
        print(znak)
        licznik += 1

if licznik == 0:
        print('Nie ma duzych liter')
else:
        print("Liczba duzych liter: ", licznik)