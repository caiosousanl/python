n = input('Digite algo ')
print('O numero é do tipo primitivo :', type(n))
print('É um número?', n.isnumeric())
print('É uma letra?', n.isalpha())
print('É uma letra ou número?', n.isalnum())
print('É Capitalizado?', n.istitle())
print('É composto por letras minúsculas?', n.islower())
print('É composto por letras maiusculas?', n.isupper())
