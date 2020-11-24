lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Insira o número na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-'*30)
print(f'Valores inseridos: {lista}')
print(f'O maior número inserido foi {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if lista[indice] == maior:
        print(f'{indice}...', end='  ')
print(f'\nO menor número inserido foi {menor}, nas posições ', end='')
for indice, valor in enumerate(lista):
    if lista[indice] == menor:
        print(f'{indice}...', end=' ')