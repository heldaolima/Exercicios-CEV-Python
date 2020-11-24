dados = {}
pessoas = []
muier = []
idadeacima = []
idades = []
somidade = 0

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if dados['Sexo'] in 'F':
        muier.append(dados['Nome'])
    dados['Idade'] = int(input('Idade: '))
    idades.append(dados['Idade'])
    somidade += dados['Idade']
    pessoas.append(dados.copy())
    resp = str(input('Continuar? ')).upper()[0]
    if resp in 'N':
        break
print(pessoas)
media = (somidade / len(pessoas))
print('--------------------------')
print(f'- Foram registradas {len(pessoas)} pessoas')
print(f'- A média de idades foi {media:.1f}')
print(f'- As mulheres registradas são: {muier}')
print(f'- Pessoas cuja idade está acima da média: ')
print()
for i, v in enumerate(idades):
    if v > media:
        for k, p in pessoas[i].items():
            print(f'{k} = {p}', end='; ')
        print()
