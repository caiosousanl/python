lista = list()
for c in range(0,5):
    lista.append(int(input(f'Digite um número na pos {c}: ')))
print(f'O maior número é {max(lista)}, na posição{lista.index(max(lista))} e o menor é {min(lista)}, '
      f'na pos {lista.index(max(lista))}')
