def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumentar(n=0, q=0):
    return n + (n * q/100)


def diminuir(n=0, q=0):
    return n - (n * q/100)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')