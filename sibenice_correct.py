import random
moznosti = ('brno', 'pariz', 'londyn')
slovo = random.choice(moznosti)
pokusy = []

def tah(vychozistav):
    pismeno = input('hadej pismeno: ')
    if pismeno in slovo:
        print('dobra volba')
        return vychozistav[:slovo.index(pismeno)] + pismeno + vychozistav[slovo.index(pismeno) + 1:]
    elif pismeno not in slovo:
        pokusy.append(pismeno)
        print('Toto jsi uz zkusil: ', pokusy)
        if len(pokusy) == 1:
            print('''
            +
            |
            |
            |
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 2:
            print('''
            +---.
            |
            |
            |
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 3:
            print('''
            +---.
            |   |
            |
            |
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 4:
            print('''
            +---.
            |   |
            |   O
            |
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 5:
            print('''
            +---.
            |   |
            |   O
            |   |
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 6:
            print('''
            +---.
            |   |
            |   O
            | --|
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 7:
            print('''
            +---.
            |   |
            |   O
            | --|--
            |
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 8:
            print('''
            +---.
            |   |
            |   O
            | --|--
            |  /
            |
            ~~~~~~~
            ''')
        elif len(pokusy) == 9:
            print('''
            +---.
            |   |
            |   O
            | --|--
            |  / \\
            |
            ~~~~~~~
            ''')
    return vychozistav


def sibenice():
    vychozistav = '_' * len(slovo)
    print(vychozistav)
    while True:
        if len(pokusy) > 9:
            print('prohral jsi')
            print('Tajne slovo bylo:', slovo)
            break
        elif '_' in vychozistav:
            vychozistav = tah(vychozistav)
            print(vychozistav)
        else:
            print('Gratuluji, vyhral jsi')
            break

sibenice()
        