lista = []
while True:
    lista.append(int(input('Insira um número: ')))
    sn = input('Continuar? [S/N]: ').strip().upper()[0]
    while sn not in 'SN':
        sn = input('Continuar? [S/N]: ').strip().upper()[0]
    if sn in 'N':
        break
print('--------------------')
print(f'Foram adicionados {len(lista)} valores')
lista.reverse()
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) > 0:
    print(f'O número 5 foi adicionado')
else:
    print('O número 5 não foi adicionado.')
