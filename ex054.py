from datetime import date
atual = date.today().year
maior = atual - 18
sa = 0
sm = 0
for c in range(1,8):
    p = int(input('em que ano a {}ª pessoa nasceu?'.format(c)))
    if p <= maior:
        sa = sa + 1
    else:
        sm = sm + 1
print('Ao todo são {} menó e {} maió'.format(sm, sa))