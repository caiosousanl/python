prime = int(input('Primeiro termo'))
r = int(input('Razão da PA'))
#a1.r0 +a1.r1 + a1.r2
for i in range(0, 10):
    print(prime + (r*i), end=' -> ')
