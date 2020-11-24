from time import sleep
from random import randint

print('-'*40)
print(f'{"GERADOR DE JOGOS":^40}')
print('-'*40)
jogos = int(input('Quantos jogos serão sorteados? '))
print(f'-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')
for j in range(0, jogos):
    numeros = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60),
               randint(1, 60)]
    print(f'Jogo {j + 1}: {numeros}')
    sleep(0.5)
    numeros.clear()
print(f'{" <BOA SORTE!> ":=^40}')
