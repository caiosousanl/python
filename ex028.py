from random import randint
r = randint(0, 5)
print('=-=' * 20)
print('Escolhi um numero entre 0 e 5, tenta advinhar qual é.')
print('=-=' * 20)
n = input('Qual numero eu escolhi? ')
#print('Acerto mizera' if n == r else 'Errou fi')
#print('Meu numero foi', r)
if n == r:
    print('Acerto mizeravi, meu numero foi', r)
else:
    print('Errrou, meu numero foi', r)