'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir ', math.hypot(ca, co))'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip2 = (co*co) + (ca*ca)
hip = hip2**(1/2)
print('A hipotenusa vai medir ',hip)
