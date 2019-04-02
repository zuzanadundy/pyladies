rychlost = int(input('Jaka je tvoje rychlost chuze? '))
if rychlost >= 130:
    print('To vypada ze spis jedes autem')
elif rychlost >= 90:
    print('Bezis rychle jako gepard')
elif rychlost >= 40:
    print('To by si mohl byt lev nebo chrt')
elif rychlost >=20:
    print('Takhle rycle beha pes')
elif rychlost >=0:
    print('Jsi zelva?')
else:
    print('Chodis pozpatku?')