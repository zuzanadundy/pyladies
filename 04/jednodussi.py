rodnecislo = '905521/4223'
cislo = (rodnecislo[0:6]) + (rodnecislo[7:11])

delenec = int(cislo)
delitel = 11

if delenec % delitel == 0:
    print('true')
else:
    print('false')