e = 0
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)
    e += 1
    lista.append(n)
    sn = str(input('Deseja continuar? [S/N] '))
    if sn in 'Nn':
        break
    while sn not in 'SsNn':
        sn = str(input('Deseja continuar? [S/N] '))
print(f'lista completa: {lista}')
print(f'lista par: {par}')
print(f'lista impar: {impar}')