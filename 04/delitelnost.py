rodnecislo = '905521/4223'
cislo = rodnecislo[0:6]
dalsi = rodnecislo[7:11]
treti = cislo + dalsi
print(treti)

cislo1= treti
cislo2 = int(cislo1)

delenec = cislo2
delitel = 11

if delenec % delitel == 0:
    print('true')
else:
    print('false')

