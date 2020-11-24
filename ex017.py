from math import sqrt

print('--- HIPOTENUSA DO TRIÂNGULO RETÂNGULO---')
adj = float(input('Insira o valor do cateto adjacente: '))
ops = float(input('Insira o valor do cateto oposto: '))
hip = sqrt(adj**2 + ops**2)
print(f'A hipotenusa mede {hip:.2f}.')
