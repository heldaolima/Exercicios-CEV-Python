from random import randint
print('-=' * 20)
print('Pensei em um número entre 0 e 5... ')
print('-=' * 20)
computador = randint(0, 5)
resp = int(input('Consegue advinhá-lo? '))
if resp == computador:
    print('PARABÉNS! Você venceu!')
else:
    print(f'Você perdeu! Pensei no número {computador}, e não no {resp}!')
