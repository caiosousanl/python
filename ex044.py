print('{:=^40}'.format(' Shop '))
produto = float(input('Digite o valor do produto:')) #{:^40} é centralizado em 40 espaços, {:=^40} c o sinal de ====
fp = int(input('''Escolha uma forma de pagamento:,
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))
if 1 <= fp <= 4:
    if fp == 1:
        print('Seu produto de R${:.2f} custará R${:.2f}'.format(produto, produto * 0.9))
    elif fp == 2:
        print('Seu produto de R${:.2f} custará R${:.2f}'.format(produto, produto * 0.95))
    elif fp == 3:
        print('Seu produto de R${:.2f} custará duas parcelas de R${:.2f}'.format(produto, produto / 2))
    elif fp == 4:
        p = int(input('Quantas parcelas?'))
        pt = produto + (0.2 * produto)
        print('Seu produto de R${} custará {} parcelas de R${}, totalizando R${}'.format(produto, p, pt / p, pt))
# juros 20% por parcela quer dizer que a cada parcela
else:
    print('Opção inválida')
