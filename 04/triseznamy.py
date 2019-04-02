zvirata = ['pes', 'kocka', 'kralik', 'had']
dalsizvirata = ['pes', 'kralik', 'krava', 'slepice']

obaseznamy = []
prvni = []

for zvire in dalsizvirata:
    if not zvire in (dalsizvirata and zvirata):
        obaseznamy.append(zvire)
print(obaseznamy)

#ukol jedna if zvire in (zvirata and dalsizvirata)
#ukol dve if not zvire in (zvirata and dalsizvirata)
#ukol dve: for zvire in dalsizvirata: if not zvire in (dalsizvirata and zvirata)
