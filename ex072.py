# Tuplas
ex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
      'seis', 'sete', 'oito', 'nove', 'dez,', 'onze',
      'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
      'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e vinte: '))
while 0 > n or n > 20:
    n = int(input('Tente novamente.\nDigite um numero entre 0 e vinte: '))
print(f'{n} por extenso é {ex[n]}')