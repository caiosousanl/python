n = (int(input('Digite um numero: ')))
print('''Escolha:
[ 1 ] se vc quiser converter pra binario,
[ 2 ] se vc quiser octal, ou
[ 3 ] se vc quiser converter pra hexadecimal.''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} em binário é:'.format(n), bin(n)[2:])
elif opcao == 2:
    print(oct(n))
elif opcao == 3:
    print(hex(n))
else:
    print('Digite um valor válido')