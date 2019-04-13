def tah(retezec, cislo_policka, symbol):
    'Vrati herni pole s danym symbolem umistenym na danou pozici'
    return retezec[:cislo_policka] + symbol + retezec[cislo_policka + 1:]
