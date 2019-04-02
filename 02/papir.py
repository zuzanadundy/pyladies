tah_pocitace = 'kamen'
tah_cloveka = input('kamen, nuzky, nebo papir? ')

if (tah_cloveka == 'kamen'and tah_pocitace == 'kamen') or (tah_cloveka == 'papir' and tah_pocitace == 'papir') or (tah_cloveka == 'nuzky' and tah_pocitace == 'nuzky'):
    print('plichta')
elif (tah_cloveka == 'kamen' and tah_pocitace == 'nuzky') or (tah_cloveka == 'nuzky' and tah_pocitace == 'papir') or (tah_cloveka == 'papir' and tah_pocitace == 'kamen'):
    print('vyhrala jsi')   
elif (tah_cloveka == 'kamen' and  tah_pocitace == "papir") or (tah_cloveka == 'nuzky' and tah_pocitace == 'kamen') or (tah_cloveka == 'papir' and tah_pocitace == 'nuzky'):
    print('pocitac vyhral')
else:
    print('nerozumim')
