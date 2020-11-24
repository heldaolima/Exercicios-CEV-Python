print('--- APROVEITAMENTO FUTEBOLÍSTICO ---')

jogador = dict()
listagol = list()
conjunto = list()
totgol = 0

while True:
    jogador['Nome'] = str(input('Nome: '))
    npartidas = int(input(f'Número de partidas jogadas por {jogador["Nome"]}: '))
    for i in range(0, npartidas):
        ngol = int(input(f'Gols feitos na {i+1} partida: '))
        listagol.append(ngol)
        totgol += ngol
    jogador['Gols'] = listagol[:]
    jogador['Total de Gols'] = totgol
    listagol.clear()
    totgol = 0
    conjunto.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resp in 'N':
        break

print('-='*30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--------------------------------------------')
for i, j in enumerate(conjunto):
    print(f'{i:>4}', end='')
    for d in j.values():
        print(f' {str(d):<15}', end='')
    print()
while True:
    vis = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if vis == 999:
        break
    if vis > (len(conjunto) - 1):
        print(f'ERRO. Não há jogador com o código {vis}.')
    else:
        print('--------------------------------------------')
        print(f'--- Levantamento do jogador {conjunto[vis]["Nome"]} ---')
        for p, g in enumerate(conjunto[vis]["Gols"]):
            print(f'    => Na partida {p+1}, fez {g} gols')
print('<< ENCERRADO >>')
