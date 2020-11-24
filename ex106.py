from time import sleep


cores = ['\033[m',        # 0 - em cor
         '\033[0;30;41m', # 1 - vermelho
         '\033[0;30;42m', # 2 - verde
         '\033[0;30;43m', # 3 - amarelo
         '\033[0;30;44m', # 4 - azul
         '\033[0;30;45m', # 5 - roxo
         '\033[7;30m'     # 6 - branco
         ]


def enfeite(text, cor=0):
    tam = len(text) + 4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'{text:^{tam}}')
    print(f'~'*tam)
    print(cores[0])
    sleep(1)


def ajuda(comando):
    enfeite(f"Accessando o manual do comando '{comando}'", 4)
    sleep(1)
    print(cores[6])
    help(comando)
    print(cores[0])
    sleep(2)


while True:
    enfeite('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando in 'fim':
        break
    ajuda(comando)

enfeite('ATÉ LOGO', 1)
