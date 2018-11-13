# max e min tuplas
from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10)
     ,randint(0, 10), randint(0, 10))
for c in n:
    print(c, end=' ' )
print(f'\nO maior numero foi', max(n))
print(f'O menor numero foi', min(n))