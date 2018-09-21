v = int(input('Velocidade do carro em Km/h: '))
m = int((v - 80)*7)
if v <= 80:
    print('Ta dboas')
else:
    print('Sifu, sua multa vai ser de', m)
