def leiaInt(entrada):
    while True:
        try:
            n = int(input(entrada))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[4;31mERRO! O usuário preferiu não informar os dados\033[m')
            return 0
        else:
            return n


def leiaFloat(entrada):
    while True:
        try:
            n = float(input(entrada))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um valor decimal válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            return 0
        else:
            break
    return n


x = leiaInt('Insira um número Inteiro: ')
y = leiaFloat('Insira um número Real: ')
print(f'Você inseriu o número inteiro {x} e o decimal {y}')
