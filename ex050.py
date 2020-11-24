soma = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'Insira o {c}º número: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print(f'Você informou {cont} valores pares, que somados resultam em {soma}')
