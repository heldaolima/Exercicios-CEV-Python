from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6)}
ranking = {}
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'  O {k} tirou {v} no dado')
    sleep(0.5)
print('------------------------------')
print('=== Ranking dos sorteados === ')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
