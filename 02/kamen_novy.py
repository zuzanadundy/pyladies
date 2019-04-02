from random import randrange
cislo = randrange(3)
if cislo == 0:      
    tah_pocitace = 'kamen'
elif cislo == 1:
    tah_pocitace = 'nuzky'
elif cislo == 2:
    tah_pocitace = 'papir'

tah_cloveka = input('kamen, nuzky, nebo papir? ')

print('tah pocitace: ', tah_pocitace)

if tah_cloveka == 'kamen':
    if tah_pocitace == 'kamen':
        print('Plichta.')
    elif tah_pocitace == 'nuzky':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'papir':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nuzky':
    if tah_pocitace == 'kamen':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'nuzky':
        print('Plichta.')
    elif tah_pocitace == 'papir':
        print('Vyhrála jsi!')
elif tah_cloveka == 'papir':
    if tah_pocitace == 'kamen':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'nuzky':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'papir':
        print('Plichta.')
else:
    print('Nerozumím.')



