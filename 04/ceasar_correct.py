plaintext = input('Zadejte text pro sifru: ')
key = int(input('Zadejte cislo jako klic pro sifru: '))
znak = ord('a')
ciphertext = ''

for sifra in plaintext:
    ciphertext += chr(((ord(sifra) - znak + key) % 26) + znak)
print(ciphertext)