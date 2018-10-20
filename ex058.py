'''t = 0
p = int(input('Digite um numero: '))
from random import randint
pc = randint(0,10)
print(pc)
while p != pc:
    if p > pc:
        print('Menos...')
        p = int(input('Tente novamente: '))
        t += 1
    if p < pc:
        print('Mais...')
        p = int(input('Tente novamente: '))
        t =+ 1
    if p == pc:
        print('Você acertou usando {} tentativas'.format(t+1))
        #meu jeito'''
from random import randint
pc = randint(0, 10)
acertou = False
while not acertou:
    p = int(input('Digite um numero de 0 a 10: '))
    if p == pc:
        acertou = True
print('Acertou')
