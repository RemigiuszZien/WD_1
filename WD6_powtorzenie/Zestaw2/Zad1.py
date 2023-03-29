with open('tekst.txt','r',encoding='utf-8') as plik:
    znaki = plik.read()[71:111]

licznik = 0
for znak in znaki:
    if znak == 'A':
        licznik += 1

if licznik == 0:
        print('Nie ma duzych liter A')
else:
        print("Liczba duzych liter A: ", licznik)