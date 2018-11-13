# palavras e vogais na tupla
palavras = ('Ameacar', 'Abelha', 'Liderar',
            'Mutacao', 'Gerar', 'Energia',
            'Midia', 'Marketing', 'Curso')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')