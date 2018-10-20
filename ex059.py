from time import sleep
op = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while op != 5 and 4:
    op = int(input('''Escolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Qual é o maior
    [4] Novos numeros
    [5] Encerrar o programa
    '''))
    print('Calculando...')
    print('-='*10)
    sleep(1.5)
    if op == 1:
        print('{}+{}={}'.format(n1, n2, (n1+n2)))
    elif op == 2:
        print('{}x{}={}'.format(n1, n2, (n1*n2)))
    elif op == 3:
        if n1>n2:
            print('{} é maior que {}'.format(n1, n2))
        if n2>n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('São iguais')
    elif op == 4:
        print('Digite novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        break
    else:
        print('Opção inválida')
print('Fim')