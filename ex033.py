a = int(input('primeiro valor '))
b = int(input('segundo valor '))  # print maior e print menor
c = int(input('terceiro valor '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior é {}, e o menor é {}'.format(maior, menor))
