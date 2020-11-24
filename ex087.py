matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatres = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira um número para a posição [{linha}; {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if coluna == 2:
            somatres += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maior = matriz[1][0]
            elif maior < matriz[1][coluna]:
                maior = matriz[1][coluna]

print('-------------------------')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('--------------------------')
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somatres}')
print(f'O maior valor da segunda linha é {maior}')
