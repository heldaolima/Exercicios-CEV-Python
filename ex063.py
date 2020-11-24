print('--- SEQUÊNCIA DE FIBONACCI ---')
n1 = 0
n2 = 1
cont = 3
termo = int(input('Até qual termo da sequência deseja ver? '))
print('------------------')
print(f'{n1} -> {n2} ', end='')
while cont <= termo:
    n3 = n1 + n2
    print(f'-> {n3} ', end='')
    n1 = n2
    n2 = n3
    cont = cont + 1
