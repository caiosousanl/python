peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura**2)
print('Seu imc de {:.2f} é'.format(imc), end=' ')
if imc <= 18.4:
    print('magrin')
elif 24.9 > imc > 18.5:
    print('normal')
else:
    print('sobrepeso')