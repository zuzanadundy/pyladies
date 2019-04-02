zvirata = ['pes', 'kocka', 'kralik', 'had']

slovo = input('zadej slovo: ')

for zvire in zvirata:
    if slovo in zvirata:
        print('true')
        break
    else:
        print('false')
        break