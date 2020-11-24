lista = []
while True:
    n = int(input('Insira um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado')
    else:
        print('Valor já informado. Não será adicionado')
    esc = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while esc not in 'SN':
        esc = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if esc in 'N':
        break
print('-------------------')
print(f'Valores adicionados em ordem: {sorted(lista)}')