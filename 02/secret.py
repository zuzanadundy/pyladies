print('Try to guess password and I will tell you a secret')
secret = input('what is the password? ')
if (secret == 'Matakia') or (secret == 'Matacek'):
    print('Well done, the secret is: Zuzi loves Alex')
elif (secret == 'Zuzi') or (secret == 'Sasi'):
    print('Almost there, try again!')
elif (secret == 'Hector') or (secret == 'Agnes'):
    print('You are close, try again')
else:
    print('Not even close, try again')