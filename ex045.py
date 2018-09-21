from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
p = int(input('''Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('='*31)
print('O computador escolheu {}'.format(itens[pc]))
print('O jogador escolheu {}'.format(itens[p]))
print('='*31)
if pc == 0:
    if p == 0:
        print('Empate')
    elif p == 1:
        print('O jogador ganhou')
    elif p == 2:
        print('O jogador perdeu')
    else:
        print('Inválido')
if pc == 1:
    if p == 0:
        print('O jogador perdeu')
    elif p == 1:
        print('Empate')
    elif p ==2:
        print('O jogador ganhou')
    else:
        print('Inválido')
if pc == 2:
    if p == 0:
        print('O jogador ganhou')
    elif p == 1:
        print('O jogador perdeu')
    elif p == 2:
        print('Empate')
    else:
        print('Opção inválida')
