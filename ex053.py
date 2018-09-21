f = str(input('''Digite uma frase para verificar se é um palindromo')
''').strip().upper())
lista = f.split()
juntar = ''.join(lista)
inverso = juntar[::-1]
if juntar == inverso:
    print('É um palindromo')
else:
    print('Nao e')
print(juntar[::-1])
#for c in range(qtd, 0 , -1):
#print(juntar[c])