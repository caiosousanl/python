# analisando nome e peso dentro de uma lista
lista = []
princ = []
maior = menor = 0
while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(float(input('Digite seu peso: ')))
    if len(princ) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    princ.append(lista[:])
    lista.clear()
    sn = str(input('Deseja continuar?[S/N] '))
    if sn in 'Nn':
        break
# print(lista, princ, len(princ))
print()
print(f'{len(princ)} foram cadastradas,')
print(f'O maior peso foi de {maior}KG, e o menor foi de {menor}Kg')
for c in princ:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')
print('foram os mais pesados')
for c in princ:
    if c[1] == menor:
        print(f'[{c[0]]}', end=' ')
print('foram os mais leves')