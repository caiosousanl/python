#analise de dados de um grupo
x = h = m = 0
while True:
    print('Cadastre uma pessoa')
    i = int(input('Idade:'))
    if i > 18:
        x += 1
    s = input('Sexo [M/F]')
    while s not in 'MmFf':
        s = input('Sexo [M/F]')
    if s in 'Mm':
        h += 1
    if i <20 and s in 'Ff':
        m =+ 1
    sn = input('Quer continuar?[S/N]')
    while sn not in 'sSnN':
        sn = input('Quer continuar?[S/N]')
    if sn in 'Nn':
        break
print(f'{x} pessoas tem mais de 18 anos')
print(f'Foram cadastrados {h} homens')
print(f'{m} mulher(es) tem menos de 20 anos')