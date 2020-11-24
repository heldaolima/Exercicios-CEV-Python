nomepeso = []
conjunto = []
maior = menor = cont = 0
while True:
    nomepeso.append((input('Nome: ')))
    nomepeso.append(float(input('Peso: ')))
    conjunto.append(nomepeso[:])
    nomepeso.clear()
    if cont == 0:
        maior = menor = conjunto[0][1]
    else:
        if conjunto[cont][1] > maior:
            maior = conjunto[cont][1]
        elif conjunto[cont][1] < menor:
            menor = conjunto[cont][1]
    cont += 1
    resp = input('Continuar? [S/N]: ').upper()[0]
    while resp not in 'SN':
        resp = input('Continuar? [S/N]: ').upper()[0]
    if resp in 'N':
        break
print('---------------------------')
print(f'Foram inseridas {cont} pessoas')
print(f'O maior peso foi {maior:.2f}Kg. Peso de: ', end='')
for pesog in conjunto:
    if pesog[1] == maior:
        print(f'[{pesog[0]}]', end=' ')
print(f'\nO menor peso foi {menor:.2f}Kg. Peso de: ', end='')
for pesop in conjunto:
    if pesop[1] == menor:
        print(f'[{pesop[0]}]', end=' ')
