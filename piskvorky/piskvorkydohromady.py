from random import randrange

def vyhodnot(retezec):
    'Vrati jednoznakovy retezec podle stavu hry'
    if 'xxx' in retezec:
        return('Vyhral pocitac') #kdyz 3 x vedle sebe, vyhral pocitac
    elif 'ooo' in retezec:
        return('Vyhral jsi') #kdyz 3 o vedle sebe, vyhral hrac
    elif '-' not in retezec:
        return('Hra je nerozhodne') #kdyz nejsou 3 stejne symboly vedle sebe a ani prazdne pole, remiza
    else:
        return('-')

def tah(retezec, cislo_policka, symbol):
    'Vrati herni pole s danym symbolem umistenym na danou pozici'
    return retezec[:cislo_policka] + symbol + retezec[cislo_policka + 1:]

def tah_hrace(retezec, dotaz):
    'vrati herni pole se zaznamenanym tahem hrace'
    while True:
        dotaz = 'Zadejte cislo policka od 1 do 19: '
        cislo_policka = int(input(dotaz)) #hrac zvoli na jake cislo policka chce dat symbol
        if cislo_policka < 0:
            print ('Nelze zadat zápornou hodnotu')
        elif cislo_policka > 19:
            print ('Pole vetsi nez 19 neexistuje')
        elif '-' not in retezec[:cislo_policka]: #retezec cislo policka z predesle funkce tah
            print('Tohle pole je uz obsazeno')
        else:
            return tah(retezec,cislo_policka,'o') #hrac bude mit vzdycky o jako svuj symbol


def tah_pocitace(retezec):
    'Vrati herni pole se zaznamenanym tahem pocitace'
    while True:
        cislo_policka = randrange(19) #pocitac nahodne vybere cislo policka
        if '-' in retezec[:cislo_policka]: #hrat na pole ktera jsou prazdna
            return tah(retezec, cislo_policka,'x') #pocitac bude mit vzdycky x jako svuj symbol
        

def piskvorky1d():
    retezec = '-' * 19 #pole = retezec z funkce tah hrace
    while '-' in retezec: #dokud jsou v poli - tak se hraje
        print(retezec)
        dotaz = 'Zadejte cislo policka od 1 do 19: '
        retezec = tah_hrace(retezec, dotaz)
        retezec = tah_pocitace(retezec)
        vyhodnoceni = vyhodnot(retezec)
        if vyhodnoceni != '-':
            print(vyhodnoceni)
            break

piskvorky1d()
