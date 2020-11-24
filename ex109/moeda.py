def dobro(n, form=False):
    dobro = n * 2
    if form:
        return moeda(dobro)
    else:
        return dobro


def metade(n, form=False):
    metade = n / 2
    if form:
        return moeda(metade)
    else:
        return metade


def aumentar(n, q, form=False):
    aumento = n + (n * q/100)
    if form:
        return moeda(aumento)
    else:
        return aumento


def diminuir(n, q, form=False):
    dimin = n - (n * q/100)
    if form:
        return moeda(dimin)
    else:
        return dimin

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
