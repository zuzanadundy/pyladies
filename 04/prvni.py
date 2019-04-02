zvirata = ['pes', 'kocka', 'kralik', 'had']
dalsizvirata = ['pes', 'kralik', 'krava', 'slepice']

prvni = []

for zvire in zvirata:
        if zvire in (zvirata and not dalsizvirata):
                prvni.append(zvire)
print(prvni)