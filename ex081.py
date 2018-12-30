e = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    e += 1
    lista.append(n)
    sn = str(input('Deseja continuar? [S/N] '))
    if sn in 'Nn':
        break
    while sn not in 'SsNn':
        sn = str(input('Deseja continuar? [S/N] '))
print(f'Você digitou {e} elementos')
lista.sort()
print(f'Em ordem crescente{lista}')
if 5 in lista:
    print(f'O numero 5 esta na lista')
