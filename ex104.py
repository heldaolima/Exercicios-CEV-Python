def leiaInt(entrada):
    n = str(input(entrada))
    if n.isnumeric():
        n = int(n)
    else:
        while not n.isnumeric():
            print('\033[4;31mERRO! Digite um valor inteiro válido.\033[m')
            n = input(entrada)
    return n


x = leiaInt('Insira um número: ')
print(f'Você acabou de inserir o número {x}')
