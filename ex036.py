casa = float(input('Valor da casa: '))
sdc = float(input('Salário do comprador: R$'))
meses = int(input('Quantos anos de financiamento? ')) * 12
prestacao = casa / meses
if prestacao > 0.30 * sdc:
    print('n vai rolar cara, sua prestação fica {:.2f}R$,'
          ' e o máximo que seria aceito seria {:.2f}R$'.format(prestacao, 0.3 * sdc))
else:
    print("vai rolar mano, sua prestação é de {:.2f}R$".format(prestacao))
