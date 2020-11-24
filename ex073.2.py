tabela2019 = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
              'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético - MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense',
              'Avaí')
print(f'Tabela do Brasileirão: {tabela2019}')
print('---------')
print(f'Os 5 primeiros colocados são: {tabela2019[:5]}')
print('---------')
print(f'Os 4 últimos são: {tabela2019[16:]}')
print('---------')
print(f'Times em ordem alfabética: {sorted(tabela2019)}')
print('---------')
print(f'O Chapecoense está na {tabela2019.index("Chapecoense")+1}º posição')
