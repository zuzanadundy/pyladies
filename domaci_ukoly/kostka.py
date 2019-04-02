import random

pocet_bodu = 0
attempt = []
attempt_two = []

while pocet_bodu < 6:
    dice = random.randint(1,6)
    print(dice)
    attempt.append(dice)
    if dice == 6:
        print('attempt:', attempt)
        print('pocet opakovani: ', (len(attempt)))
        break

while pocet_bodu < 6:
    dice = random.randint(1,6)
    print(dice)
    attempt_two.append(dice)
    if dice == 6:
        print('attempt two:', attempt_two)
        print('pocet opakovani 2: ', (len(attempt_two)))
        break

if len(attempt) > len(attempt_two):
    print('vyhral hrac jedna')
else:
    print('vyhral hrac dve')
