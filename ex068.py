from random import randint
contw = 0
print('-='*15)
print('        PAR OU ÍMPAR     ')
print('-='*15)
print()
while True:
    n = int(input('Insira um número: '))
    pi = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    pc = randint(0, 10)
    result = n + pc
    print('-'*40)
    print(f'Você jogou {n} e o computador jogou {pc}. Total de {result}')
    print('-'*40)
    if pi in 'P':
        if result % 2 == 0:
            print('DEU PAR! Você VENCEU!')
            print('Vamos jogar novamente...')
            contw += 1
        else:
            print(f'Deu ÍMPAR! GAME OVER... ', end='')
            break
    elif pi in 'I':
        if result % 2 == 0:
            print('DEU PAR! GAME OVER... ', end='')
            break
        else:
            print('DEU ÍMPAR! Você VENCEU!')
            contw += 1
    print('-'*40)
if contw == 0:
    print('Você não venceu nenhuma vez.')
elif contw == 1:
    print('Você venceu 1 vez!')
else:
    print(f'Você venceu {contw} vezes!!')
