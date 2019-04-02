rodnecislo = '906221/4223'

treticislo = rodnecislo[2]

for i in treticislo:
    if i == '6':
        treticislo = ('1' + rodnecislo[3])
        print(treticislo)
        break

if (rodnecislo[2] == '5'):
    print(rodnecislo [4:6], '/', rodnecislo[3], '/', rodnecislo[0:2])
elif (rodnecislo[2]) == '6':
    print(rodnecislo [4:6], '/', treticislo, '/', rodnecislo[0:2])
else:
    print(rodnecislo [4:6], '/', rodnecislo[2:4], '/', rodnecislo[0:2])

