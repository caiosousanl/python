#maior e menores, media e contagem while
s = 0
n = int(input('Digite um número: '))
sn = input('Deseja continuar?[S/N]')
cont = 1
s =+ n
maior = menor = n
while sn in 'Ss':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    else:
        menor = menor = n
    cont += 1
    s += n
    sn = input('Deseja continuar?[S/N]').upper().strip()
media = s / cont
print('Você digitou {} numeros, a media entre eles foi {}'.format(cont, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
