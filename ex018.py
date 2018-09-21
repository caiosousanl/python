import math
a = float(input('Digite um angulo: '))
print('O seno, cosseno, e tangente de {} medem respectivamente'.format(a))
print('{}, {} e {}'.format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
