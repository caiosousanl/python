from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
if idade <= 9:
    print('Mirin')
elif 14 >= idade > 9:
    print('Infantil')
elif 19 >= idade > 14:
    print('Junior')
elif 25 >= idade >19:
    print('Senior')
else:
    print('Master')