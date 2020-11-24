print('--- EMPRÉSTIMOS ---')
casa = float(input('Qual o valor da casa a ser comprada? R$'))
sal = float(input('Qual o  valor do salário do comprador? R$'))
anos = int(input('Em quantos anos ele pretende pagar? '))
prest = casa / (anos * 12)
limite = sal * (30/100)
print('=-=-=-=-=-')
print(f'A prestação de uma casa de R${casa:.2f} em {anos} anos custa R${prest:.2f}.')
if prest <= limite:
    print('Muito bem. O empréstimo será concedido')
else:
    print('Empréstimo negado.')
