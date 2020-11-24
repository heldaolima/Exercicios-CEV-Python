from time import sleep

def linha(tam=42):
    return '-' * tam


def titulo(msg, tam=42):
    print(linha())
    print(f'{msg:^{tam}}')
    print(linha())


def individcor(txt, cor=0):
    return f'{colorido(cor)}{txt} {colorido(0)}'


def colorido(cod):
    lst = ['\033[m',        # 0 - sem cor
           '\033[0;31m',    # 1 - Vermelho
           '\033[0;32m',    # 2 - Verde
           '\033[0;33m',    # 3 - Amarelo
           '\033[0;34m']     # 4 - Azul
    return lst[cod]


def leiaInt(entrada, max=False, cor=0):
    while True:
        try:
            n = int(input(individcor(entrada, cor)))
            if max:
                if n > max:
                    print(individcor('ERRO! Por favor, insira uma opção válida.', 1))
                    continue
        except (TypeError, ValueError):
            print(individcor('ERRO! Por favor, insira um número inteiro válido', 1))
        else:
            return n


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{individcor(c, 2)} - {individcor(item, 4)}')
        c += 1
    print(linha())
