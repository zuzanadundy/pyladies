def tah_hrace(retezec, dotaz):
    'vrati herni pole se zaznamenanym tahem hrace'
    while True:
        cislo_policka=int(input(dotaz))
        if cislo_policka < 0:
            print ('Nelze zadat zápornou hodnotu')
        elif cislo_policka > 19:
            print ('Pole vetsi nez 19 neexistuje')
        elif '-' not in retezec[:cislo_policka]:
            print('Tohle pole je uz obsazeno')
        else:
return tah(retezec,cislo_policka,'x')