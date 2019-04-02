from random import randrange

pocet_bodu = 0
while pocet_bodu < 21: 
    print('Ted mate bodu', pocet_bodu) #Počítač v každém kole vypíše, kolik máš bod
    pokracovat = input('chcete pokracovat?') # zeptá se tě, jestli chceš pokračovat.
    if pokracovat == 'ano': #„ano“, počítač „otočí kartu“
        karta = randrange (2, 10) #náhodně vybere číslo od 2 do 10
        print (karta + pocet_bodu) #vypíše její hodnotu a přičte ji k bodům.
    elif pokracovat == 'ne':
        print('hra skoncila')
        break
    else:
        print('odpovidej ano/ne') 

    if pocet_bodu == 21
        print('vyhral jsi')
    
    else pocet_bodu > 21
        print('prohral jsi')
    