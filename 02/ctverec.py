#tento program pocita obvod a obsah ctverce
strana = float(input("zadej cislo "))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print("obvod ctverce se stranou", strana, "cm je", 4 * strana, "cm")
    print("obsah ctverce se stranou", strana, "cm je", strana * strana, "cm2")
else: 
    print("zadej kladne cislo")
print("dekuju za pouziti kalkulacky")


