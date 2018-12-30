lista = []
pares = []
impares = []
for p in range(1, 8):
    valor = input(f'Digite o {p}º valor:')
    if valor % 2 == 0:
        pares.append()
    if p % 2 != 0:
        impares.append(input(f'Digite o {p}º valor:'))
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')