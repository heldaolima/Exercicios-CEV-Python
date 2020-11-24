print('--- CALCULADOR DE DESCONTO ---\n')
prod = float(input('Qual o preço produto em questão? R$'))
desc = (5/100) * prod
final = prod - desc
print('----')
print(f'Estamos oferecendo 5% de desconto. Serão descontados R${desc:.2f}.\n'
      f'Portanto, a sua compra terá novo valor de R${final:.2f}.')