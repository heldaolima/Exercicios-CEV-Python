escolha = 0
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
while escolha != 5:
    print('-----------------')
    print('''Opções:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] DESCOBRIR QUAL É O MAIOR
        [4] INSERIR NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
    escolha = int(input('O que deseja fazer? '))
    if escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}.')
    elif escolha == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif escolha == 3:
        if n1 != n2:
            print(f'Entre {n1} e {n2}, ', end='')
            if n1 > n2:
                print(f'{n1} é maior.')
            elif n2 > n1:
                print(f'{n2} é maior.')
        else:
            print('Os valores inseridos são iguais.')
    elif escolha == 4:
        print('Trabalhando nisso... ')
        n1 = float(input('Insira o novo primeiro valor: '))
        n2 = float(input('Insira o novo segundo valor: '))
    elif escolha == 5:
        print('Programa encerrado.')
    else:
       print('Insira uma opção válida: ')
print('Até mais')