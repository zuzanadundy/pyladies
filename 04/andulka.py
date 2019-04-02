zvirata = ['pes', 'kocka', 'kralik', 'had', 'andulka']

novazvirata = []

for zvire in zvirata:
    zvire = (zvire[1:])
    novazvirata.append(zvire)
    novazvirata.sort()
print(novazvirata)


