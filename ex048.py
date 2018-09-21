soma = 0
cont = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        soma = soma + s #pode ser escrito como soma += s
        cont = cont + 1
print('A soma de {} valores é {}'.format(cont, soma))
