s = float(input('Salário atual: ')) #pra usar duas casas decimais o comando é {:.2f}
if s > 1250:
    print('Seu novo salário sera de: {:.2f}'.format(s*1.10))
else:
    print('Seu novo salário será de: {:.2f}'.format(s*1.15))