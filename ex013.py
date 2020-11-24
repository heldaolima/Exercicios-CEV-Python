print('--- CALCULADOR DE REAJUSTES ---\n')
salario = float(input('Insira o salário atual do funcionário: R$'))
aum = float(salario * 15/100)
final = salario + aum
print('----')
print(f'O aumento de 15% valerá R${aum:.2f}\n'
      f'O valor final do salário será R${final:.2f}')
