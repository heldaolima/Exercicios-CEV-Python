print('--- FATORIAL ---')
num = int(input('Insira um número: '))
cont = num
fat = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')
