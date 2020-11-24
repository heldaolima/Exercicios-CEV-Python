from ex109 import moeda

pre = float(input('Insira o preço: R$'))
print('--------------')
print(f'O valor {moeda.moeda(pre)} dobrado vale {moeda.dobro(pre, True)}')
print(f'A metade de {moeda.moeda(pre)} é {moeda.metade(pre, True)}')
print(f'10% aumentado: {moeda.aumentar(pre, 10, True)}')
print(f'20% diminuido: {moeda.diminuir(pre, 20, True)}')
