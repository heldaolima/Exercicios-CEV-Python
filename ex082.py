lista = []
pares = []
impares = []
while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    sn = input('Continuar? [S/N]: ').upper()[0]
    while sn not in 'SN':
        sn = input('Continuar? [S/N]: ').upper()[0]
    if sn in 'N':
        break
print('-------------------------')
print(f'Todos os números: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
