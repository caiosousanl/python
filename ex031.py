d = float(input('Distância em Km: '))
#if d<=200:
#    p = d*(0.50)
#    print('O preço será',p)
#else:
#    p = d*(0.45)
#    print('O preço será' ,p)
p = d * 0.5 if d<=200 else 0.45 * d
print(p,'Reais')