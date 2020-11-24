from datetime import datetime

dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nasicmento: '))
anoatual = datetime.today().year
dados['Idade'] = anoatual - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Idade de Aposentadoria'] = (dados['Ano de Contratação'] + 35) - nasc
print('-='*30)
print(dados)
for k, v in dados.items():
    print(f' --{k}: {v}')
