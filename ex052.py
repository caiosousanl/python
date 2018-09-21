#ver se é primo
tot = 0
num = int(input('Digite um numero: '))
#pra ser primo tem q ser devisivel por 1 e por ele mesmo
print('='*30)
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot +1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO numero {} foi dividido {} vezes'.format(num,tot))
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')