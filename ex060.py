'''from math import factorial
f = int(input('Digite o fatorial'))                5! = 5 * 4 * 3 * 2 * 1
print('O fatorial de {} é {}'.format(f, factorial(f)))'''
n = int(input('Digite o fatorial'))
f = 1
while n > 0:
    print(n, end='')
    print('x' if n >1 else '=', end='')
    f = f * n
    n -= 1
print(f)