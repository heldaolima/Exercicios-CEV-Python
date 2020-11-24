print('--- APROVEITAMENTO FUTEBOLÍSTICO ---')

jogador = dict()
totgol = 0
listagol = list()

jogador['Nome'] = str(input('Nome: '))
npartidas = int(input(f'Número de partidas jogadas por {jogador["Nome"]}: '))
for i in range(0, npartidas):
    ngol = int(input(f'Gols feitos na {i+1} partida: '))
    listagol.append(ngol)
    totgol += ngol
jogador['Gols'] = listagol
jogador['Total de Gols'] = totgol

print('-----------------------------')
print(jogador)
print('-----------------------------')

for k, v in jogador.items():
    print(f'{k}: {v}')
print('-----------------------------')
print(f'O jogador {jogador["Nome"]} jogou {npartidas} partidas.')
for p, g in enumerate(listagol):
    print(f'    => Na partida {p+1}, fez {g} gols')
print(f'Foi um total de {totgol} gols')
