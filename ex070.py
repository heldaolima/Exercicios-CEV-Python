tot = 0
contpreco = 0

produto = input('Nome do produto: ')
preco = float(input('Preço: R$'))
if preco > 1000:
    contpreco = 1
tot += preco
menorval = preco
menornome = produto
print('-'*20)
escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
while escolha not in 'SN':
    escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
print('-'*20)
if escolha in 'S':
    while True:
        produto = input('Nome do produto: ')
        preco = float(input('Preço: R$'))
        if preco > 1000:
            contpreco += 1
        tot += preco
        if preco < menorval:
            menorval = preco
            menornome = produto
        print('-'*20)
        escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
        while escolha not in 'SN':
            escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
        if escolha in 'N':
            break
        print('-'*20)
print('-'*20)
print(f'Total gasto na compra: R${tot:.2f}')
print(f'Total de produtos que custam mais de R$1000.00: {contpreco}')
print(f'Produto mais barato: {menornome}, que custa R${menorval:.2f}')
