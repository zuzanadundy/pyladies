kosik = {'jabko': 'cervene', 'hruska': 'zelena', 'broskev': 'oranzova', 'banan': 'zluty'}

shnily_kosik = {}


for klic, hodnota in kosik.items():
    shnily_kosik[klic] = 'hnědo-' + hodnota

print(shnily_kosik)
