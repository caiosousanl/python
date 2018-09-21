s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Valor {}:'.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma de {} numeros pare é {}'.format(cont, s))
