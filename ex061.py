a0 = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 0

while not cont == 10:
    if cont == 0:
        print(a0, end=' -> ')
        cont += 1
    else:
        print(a0+(r*cont), end='')
        print(end=' -> ' if cont < 10 else ' ' )
        cont += 1
print('Fim' if cont == 10 else '')