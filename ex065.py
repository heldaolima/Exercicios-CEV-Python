soma = maior = menor = cont = 0
resp = 'S'
while resp in 'S':
    n = float(input('Insira um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
print('----------')
media = soma / cont
print(f'A média dos valores inseridos foi {media:.2f}')
print(f'O menor valor inserido foi {menor}')
print(f'O maior valor inserido foi {maior}')
