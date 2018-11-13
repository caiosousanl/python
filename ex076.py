# Lista de preços com tuplas
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 20,
            'Estojo', 15,
            'Transferidor', 2,
            'Compasso', 6,
            'Mochila', 259.99,
            'Canetas', 22.30,
            'Livros', 670.50)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:.>7.2f}')