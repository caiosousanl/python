#Jogo par ou ímpar
from random import randint
v = 0
while True:
    pc = randint(0, 10)
    j = int(input('Digite um valor: '))
    r = pc + j
    pi = ' '
    while pi not in 'pi':
        pi = str(input('Par ou Ímpar? ')).strip().lower()[0]
    print('-'*20)
    print(f'Você = {j} Computador = {pc}\nTotal = {r}')
    print('-' * 20)
    print(f'{r} é impar, ' if r % 2 == 1 else f'{r} é par, ', end='')
    if pi == 'p':
        if r % 2 == 0:#é par
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    elif pi == 'i':
        if r % 2 == 1: #éimpar
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
print(f'Você acertou {v} vezes.')
