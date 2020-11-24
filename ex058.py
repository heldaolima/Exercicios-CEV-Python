from random import randint

print('--- JOGUINHO 2.0 ---')
print('-=' * 20)
print('Pensei em um número entre 0 e 5... ')
print('-=' * 20)
computador = randint(0, 10)
resp = int(input('Consegue advinhá-lo? '))
cont = 1
while resp != computador:
    resp = int(input('ERRADO! Tente novamente: '))
    cont += 1
if cont == 1:
    tent = 'tentativa'
else:
    tent = 'tentativas'
print(f'CORRETO! Parabéns, depois de {cont} {tent} você conseguiu!')
