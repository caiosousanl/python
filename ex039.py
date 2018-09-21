from datetime import date
atual = date.today().year
ano = int(input('Quando q tu nasceu? '))
if ano == 2000:
    print('Você deve se alistar esse ano({})'.format(atual))
elif ano > 2000:
    print("Você deverá se alistar em {}".format(ano + 18))
if ano < 2000:
    print('Voce deveria ter se alistado no ano {}'.format(ano + 18))
