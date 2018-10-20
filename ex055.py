maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            p = maior
        if p < menor:
            menor = p
print('A pessoa mais pesada pesa: {}Kg'.format(maior))
print('A pessoa mais leve pesa: {}Kg'.format(menor))
