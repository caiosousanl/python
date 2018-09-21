n1 = int(input('Digite qualquer numero:'))
n2 = int(input('Digite qualquer numero:'))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
if n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('\033[4;1;44mSão iguais\033[m')