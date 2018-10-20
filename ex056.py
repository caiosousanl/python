si = 0
maiori = 0
nvelho = ''
nmnovas = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    n = str(input('Nome: ').strip())
    i = int(input('Idade: '))
    s = str(input('Sexo (M/F):')).strip()
    si += i
    if i < 20 and s in 'Ff':
        nmnovas += 1
    if p == 1 and s in 'Mm':
        maiori = i
        nvelho = n
    if i > maiori and s in 'Mm':
            maiori = i
            nvelho = n
print('A media das idades foi', si/4)
print('O mais velho foi {} com {} anos'.format(nvelho, maiori))
print('{} mulheres tem menos de 20 anos'.format(nmnovas))