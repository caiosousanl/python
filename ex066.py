#utilizando break
s = c = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma entre {c} números é de {s}')
