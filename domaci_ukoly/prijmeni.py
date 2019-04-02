prijmeni = input('zadej sve prijmeni: ')

for i in prijmeni:
    if prijmeni[-3:] == 'ova':
        print('jsi zena')
    else:
        print('jsi muz')
    break
