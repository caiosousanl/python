nome = str(input('Digite seu nome completo: ').strip())
nomeup = nome.upper()
#nome = input('Digite seu nome: ')
#print(nome.lower())                                     #41:30 curso
#nome = input('Digite seu nome: ')
#print(len(nome))
print('Seu nome maiusculo é : {}'.format(nomeup))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' '))) #o . count mostra quantas vezes o valor colocado aparece
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))# o .find mostra a posição valor colocado