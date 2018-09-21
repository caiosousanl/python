'''A soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado;'''
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a < b + c and b < (c + a) and c < (a + b) :
    print('Pode ser um triângulo')
else:
    print('Nao pode ser')