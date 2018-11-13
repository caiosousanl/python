# contador de cédulas de um caixa eletrônico 1.0
v = int(input('Qual será o valor a ser sacado? '))
# 1 2 5 10 20 50 100 cédulas
n100 = (v // 100)
n50 =  (v - n100*100) //50
n20 =  (v - n100*100 - n50*50) //20
n10 =  (v - n100*100 - n50*50 - n20*20) //10
n5 =   (v - n100*100 - n50*50 - n20*20 - n10*10 ) // 5
n2 =   (v - n100*100 - n50*50 - n20*20 - n10*10 - n5 *5 ) //  2
n1 =   (v - n100*100 - n50*50 - n20*20 - n10*10 - n5 *5 - n2 * 2 ) // 1
print(f'{n100} cedulas de 100\n{n50} cédulas de 50\n{n20} cédulas de 20'
      f'\n{n10} cédulas de 10\n{n5} cédulas de 5\n{n2} '
      f'cédulas de 2\n{n1} cedula de 1')