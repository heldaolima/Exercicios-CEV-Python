print('--- BASES NUMÉRICAS ---')
n = int(input('Insira o número inteiro: '))
print('''Você pode convetê-lo para:
    [ 1 ] BINÁRIO
    [ 2 ] OCTAL
    [ 3 ] HEXADECIMAL''')
resp = int(input('Sua opção (outro valor encerra o programa):  '))
print('-------------')
if resp == 1:
    print(f'{n} convertido para \033[4mbinário\033[m é: {bin(n)[2:]}')
elif resp == 2:
    print(f'{n} convertido para \033[4moctal\033[m é: {oct(n)[2:]}')
elif resp == 3:
    print(f'{n} convertido para \033[4mhexadecimal\033[m é: {hex(n)[2:]}')
else:
    print('Você encerrou o programa.')
