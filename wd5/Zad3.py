with open('plikk.txt','r+') as f:
    f.write('linjika 1\n')
    f.write('linijka 2\n')
    f.write('linijka 3\n')
    print(f.readlines())