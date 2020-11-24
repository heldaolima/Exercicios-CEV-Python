tabela2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Os \033[4m5 primeiros colocados\033[m do Camepeonato Brasileiro de Futebol 2019:')
for i in range(0, 5):
    print(f'{i+1}º: {tabela2019[i]}')
print('-----------')
print('Os \033[4m4 últimos colocados\033[m: ')
for u in range(16, 20):
    print(f'{u+1}º: {tabela2019[u]}')
print('-----------')
print('Os 20 classificados \033[4mem ordem alfabética\033[m:')
for alfa in sorted(tabela2019):
    print(alfa)
print('-----------')
print(f'O Chapecoense está na {tabela2019.index("Chapecoense") + 1}º posição')
