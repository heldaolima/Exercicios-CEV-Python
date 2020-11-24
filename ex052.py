print('--- NÚMEROS PRIMOS ---')
num = int(input('Insira um número inteiro: '))
tot = 0

for i in range(1, num+1):
    if num % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')

print(f'\n\033[mO número {num} foi dividido {tot} vezes.')
if tot == 2:
    print('Ele é primo.')
else:
    print('Ele não é primo')
