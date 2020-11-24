print('--- CALCULADOR DE AUMENTO ---')
sal = float(input('Insira o salário atual: R$'))

if sal > 1250:
    aum = sal * 10/100
    tot = sal + aum
else:
    aum = sal * 15/100
    tot = sal + aum

print(f'O aumento será no valor de R${aum:.2f}. O novo salário será R${tot:.2f}')
