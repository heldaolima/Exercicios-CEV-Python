print('=' * 15, ' TABUADA v2.0 ', '=' * 15)
n = int(input('Insira o número cuja tabuada você quer ver: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
