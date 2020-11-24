from datetime import date

print('--- ALISTAMENTO ---')
nasc = int(input('Insira o seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - nasc
print('-------------')

if idade < 18:
    saldo = 18 - idade
    print(f'Aos {saldo} anos, ', end='')
    if saldo != 1:
        print(f'faltam {saldo} anos para que você possa se alistar.')
    elif saldo == 1:
        print(f'falta 1 ano para que você possa se alistar. ')
    print(f'O seu alistamento será em {saldo + hoje}')
elif idade == 18:
    print('Você está na idade do alistamento obrigatório. Dirija-se ao quartel mais próximo.')
else:
    saldo = idade - 18
    print(f'Aos {idade} anos, você passou ', end='')
    if saldo != 1:
        print(f'{saldo} anos da idade do alistamento obrigatório.')
    elif saldo == 1:
        print(f'1 ano da idade do alistamento obrigatório.')
    print(f'O seu alistamento foi em {hoje - saldo}')
