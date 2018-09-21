algo = str(input('Falai ')).strip().lower()
print('A letra A aparece {} vezes'.format(algo.count('a')))
print('A primeira vez q A aparece é na posição', (algo.find('a') + 1))
print('A ultime é na', algo.rfind('a') + 1)