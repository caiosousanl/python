s = str(input('Digite seu sexo[M/F]')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Tente novamente:'))
print('sexo {} salvo.'.format(s))
