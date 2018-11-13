#estatísticas de produtos de um supermercado
t = c  = cont = menor = 0
b = ''
while True:
    n = input('Digite o nome do produto: ')
    p = int(input('Digite quanto custa o produto: R$'))
    cont += 1
    if p > 1000:
        c += 1
    t += p
    if cont == 1:
        menor = p
        b = n
    else:
        if p < menor:
            menor = p
            b = p

    sn = input('Quer continuar ?[S/N]')
    while sn not in 'sSnN':
        sn = input('Quer continuar ?[S/N]')
    if sn in 'Nn':
        break
print(f'O total gasto foi {t}')
print(f'{c} produtos custam mais de 1000R$')
print(f'"{b}" é o produto mais barato, custando R${menor}')