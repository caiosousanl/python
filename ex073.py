times = ('Palmeiras', 'Inter', 'Flamengo','São Paulo',
         'Gremio', 'Atletico-MG', 'Santos', 'Cruzeiro',
         'Atlético-PR', 'Fluminense', 'Bahia', 'Corinthias',
         'Vasco', 'Botafogo', 'Ceará', 'Sport', 'Vitória',
         'América', 'Chapecoense', 'Paraná')
print('='*40)
print(f'Os 5 primeiros classificados:\n{times[:5]}')
#for t in times:
    #print(t)
print('='*40)
print(f'Os 4 últimos colocados:\n{times[-4:]}')
print('='*40)
print(f'Times em ordem alfabética:\n{sorted(times)}')
print('='*40)
print(f'Chapecoense está na posição:\n{times.index("Chapecoense")+1}')
print('='*40)