from random import randrange

pocet_bodu = 0 #Začínáš s 0 body.
while pocet_bodu < 21: #dokud mensi nez 21 tak se hraje
    print('Ted mate bodu', pocet_bodu) #Počítač v každém kole vypíše, kolik máš bod
    pokracovat = input('chces pokracovat?') # zeptá se tě, jestli chceš pokračovat.
    if pokracovat == 'ano': #„ano“, počítač „otočí kartu“
        karta = randrange (2, 11) #náhodně vybere číslo od 2 do 10, (musim dat cislo 11)
        pocet_bodu = pocet_bodu + karta #soucet predeslych pocet bodu a nove karty
        print ('mas kartu', karta) #vypíše její hodnotu
    elif pokracovat == 'ne': #Pokud odpovíš „ne“, hra končí.
        print('hra skoncila')
        break
    else:
        print('odpovidej ano/ne') 

    if pocet_bodu == 21: #21 vyhrava
        print('vyhral jsi')
    
    elif pocet_bodu > 21: #hraje se do 21
        print('prohral jsi')
