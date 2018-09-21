s1 = float(input('Digite o valor do seguimento 1: '))
s2 = float(input('Digite o valor do seguimento 2: '))
s3 = float(input('Digite o valor do seguimento 3: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Pode formar triangulo', end=' ') # o end = 'nada' pula pra linha de baixo
    if s1 == s2 == s3:
        print('equilátero')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Nao forma triangulo')
