print('--- CÁLCULO DE GASTO DE TINTA ---\n')
larg = float(input('Insira a largura da parede: '))
alt = float(input('Insira a altura da parede: '))
area = float(larg * alt)
tinta = area / 2
print('------')
print(f'A área da parede vale {area:.3f}m^2.\n'
      f'1L de tinta pinta 2m^2; serão necessários {tinta:.4f}L para pintar a parede.')
