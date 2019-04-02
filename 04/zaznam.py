zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

spravne_zaznamy = []
spatne_zaznamy= []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne_zaznamy.append(zaznam)

print(spravne_zaznamy)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if jmeno[0].islower() or prijmeni[0].islower():
        spatne_zaznamy.append(zaznam)

print(spatne_zaznamy)

#else:spatne.append(zaznam)

opravne_zaznamy= []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split(' ')
    jmeno = jmeno, prijmeni[0]
    prijmeni = jmeno, prijmeni[1]
    opravne_zaznamy.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())

    print(opravne_zaznamy)