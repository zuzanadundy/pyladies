zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

chybne_zaznamy = []
for zaznam in zaznamy:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    if jmeno[0].islower() or prijmeni[0].islower():
        chybne_zaznamy.append(zaznam)
print(chybne_zaznamy)

spravne_zaznamy = []
for zaznam in zaznamy:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne_zaznamy.append(zaznam)
print(spravne_zaznamy)

opravene_zaznamy = []
for zaznam in zaznamy:
    jmeno_a_prijmeni = zaznam.split(' ')
    jmeno = jmeno_a_prijmeni[0]
    prijmeni = jmeno_a_prijmeni[1]
    opravene_zaznamy.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
print(opravene_zaznamy)