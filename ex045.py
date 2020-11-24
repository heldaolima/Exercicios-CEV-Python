from random import randint
from time import sleep

print('--- JOKENPÔ ---')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
enfeite = '-=' * 15
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Faça a sua jogada: '))
pc = randint(0, 2)
if jogada == 0 or jogada == 1 or jogada == 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!')
    sleep(0.5)
    print(enfeite)
    print(f'''JOGADOR joga {itens[jogada]}
COMPUTADOR joga {itens[pc]}''')
    print(enfeite)
else:
    print()
if jogada == 0:
    if pc == 0:
        print('EMPATE!')
    elif pc == 1:
        print('VITÓRIA DA MÁQUINA!')
    else:
        print('VITÓRIA DO JOGADOR!')
elif jogada == 1:
    if pc == 0:
        print('VITÓRIA DO JOGADOR!')
    elif pc == 1:
        print('EMPATE!')
    else:
        print('VITÓRIA DA MÁQUINA!')
elif jogada == 2:
    if pc == 0:
        print('VITÓRIA DA MÁQUINA')
    elif pc == 1:
        print('VITÓRIA DO JOGADOR!')
    else:
        print('EMPATE!')
else:
    print('Opção inválida. Tente novamente.')
