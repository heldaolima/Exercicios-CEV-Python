from ex107 import moeda

pre = float(input('Insira o preço: R$'))
print(f'O valor {pre} dobrado vale {moeda.dobro(pre)}')
print(f'A metade de {pre} é {moeda.metade(pre)}')
print(f'10% aumentado: {moeda.aumentar(pre, 10)}')
print(f'20% diminuido: {moeda.diminuir(pre, 20)}')
