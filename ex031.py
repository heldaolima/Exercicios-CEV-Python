print('--- CALCULADOR DE PASSAGEM ---')
viagem = float(input('Qual a distância da viagem? Km '))

if viagem > 200:
    passagem = viagem * 0.45
    print(f'Para a distância de {viagem} km, passagem custa R$0.45 por km.')
else:
    passagem = viagem * 0.50
    print(f'Para a distância de {viagem} km, a passagem vusta R$0.50 por km.')

print(f'Portanto, a sua passagem custará R${passagem:.2f}')
