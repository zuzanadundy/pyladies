def vyhodnot(radek):
    'Vrati jednoznakovy retezec podle stavu hry'
    if 'xxx' in radek:
        return('x')
    elif 'ooo' in radek:
        return('o')
    elif '-' not in radek:
        return('!')
    else:
        return('-')