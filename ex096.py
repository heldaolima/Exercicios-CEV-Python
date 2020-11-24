def area(larg, comp):
    result = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {result:.1f}m^2')


print('Controle de Terrenos')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
