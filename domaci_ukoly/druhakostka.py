import random

pocet_bodu = 0
hody = []

while pocet_bodu < 6:
    kostka = random.randint(1,6)
    print(kostka)
    
    hody.append(kostka)
    print('hody:', hody)
    opakovani = hody.count(kostka)
    print('pocet opakovani: ', opakovani)
    if kostka == 6:
    break