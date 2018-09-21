from datetime import date
ano = float(input('Digite um ano: '))
if ano == 0: #nem terminei
    print('É bissexto' if (ano%4)==0 and ano%100 != 0 or ano%400 ==0 else 'Não é')