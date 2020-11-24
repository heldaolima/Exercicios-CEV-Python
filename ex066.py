cont = 0
soma = 0
while True:
    n = int(input('Insira um número (999 encerra): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} números inseridos vale {soma}')
