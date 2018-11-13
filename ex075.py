t = (int(input('Digite o primeiro numero')),
     int(input('Digite o segundo numero')),
     int(input('Digitre o terceiro numero')),
     int(input('Digitre o quarto numero')))
print(t)
print(f'O numero 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na posição {t.index(3)}')
else:
    print(f'O valor 3 não apareceu')
print(f'Valores pares digitados: ', end='')
for n in t:
    if n % 2 == 0:
        print(n,end=' ')
