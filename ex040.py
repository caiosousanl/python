n1 = float(input('Nota do primeiro semestre: '))
n2 = float(input('Nota do segundo semestre: '))
m = (n1 + n2) / 2
print(m)
if m > 7:
    print('Aprovado')
elif 5 >= m > 6.9 :
    print('Recuperação')
else:
    print('Reprovado')