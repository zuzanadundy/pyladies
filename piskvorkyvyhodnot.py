def vyhodnot(retezec):
    'Vrati jednoznakovy retezec podle stavu hry'
    if 'xxx' in retezec:
        return('x')
    elif 'ooo' in retezec:
        return('o')
    elif '-' not in retezec:
        return('!')
    else:
        return('-')