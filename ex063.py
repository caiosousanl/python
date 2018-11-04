#sequencia de Fibonacci 0 1 1 2 3 5 8 13
n = int(input('Digite um numero'))
termo1 = 0
termo2 = 1
cont = 3
print(termo1,'->', termo2, end='')
while cont <=n:
    termo3 = termo1 + termo2
    print(' ->', termo3, end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('\nFim')