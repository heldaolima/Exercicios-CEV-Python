from ex108 import moeda

pre = float(input('Insira o preço: R$'))
print('--------------')
print(f'O valor {moeda.moeda(pre)} dobrado vale {moeda.moeda(moeda.dobro(pre))}')
print(f'A metade de {moeda.moeda(pre)} é {moeda.moeda(moeda.metade(pre))}')
print(f'10% aumentado: {moeda.moeda(moeda.aumentar(pre, 10))}')
print(f'20% diminuido: {moeda.moeda(moeda.diminuir(pre, 20))}')
