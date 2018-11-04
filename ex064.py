#soma de termos
n = s = cont = 0
n = int(input('Digite um numero(999 para parar)'))
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um numero(999 para parar)'))
print('A soma dos {} numeros é'.format(cont), s)