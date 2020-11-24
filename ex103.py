def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if g.isnumeric():
        gols = int(g)
    else:
        gols = 0
    print('------------------------')
    print(f'O jogador {nome} fez {gols} gols')

j = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
ficha(j, g)
