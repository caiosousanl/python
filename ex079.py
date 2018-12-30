lista = []
sn = 's'
while sn in 'sim':
    v = int(input('Digite um valor: '))
    while v in lista:
        v = input('Digite um valor diferente do que ja está na lista: ')
    lista.append(v)
    sn = input('Quer continuar? [S/N]').lower()
    while sn not in 'simnaão':
        sn = input('Quer continuar? [S/N]').lower()
lista.sort()
print(lista)