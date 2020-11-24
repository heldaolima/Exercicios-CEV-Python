cont = soma = 0
n = float(input('Insira um número [999 encerra]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Insira um número [999 encerra]: '))
print('---------------')
print(f'A soma dos {cont} números inseridos vale {soma}')
