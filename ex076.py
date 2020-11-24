produtos = ('Lápis', 1.00, 'Borracha', 1.50, 'Caderno', 3.50, 'Estojo', 15.00, 'Transferidor', 4.32, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 5.25, 'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS ":^40}')
print('-'*40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R$ {produtos[i]:>7.2f}')