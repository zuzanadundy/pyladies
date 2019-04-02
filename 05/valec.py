from math import pi

def obsah_elipsy(a, b):
    "Vrati obsah elipsy danych rozmeru"
    return pi * a * b


def obsah_valce (a, b, vyska):
    "vrati obsah eliptickeho valce"
    obsah = obsah_elipsy(a, b)
    return (obsah * vyska)


print(obsah_valce(4, 5, 6))