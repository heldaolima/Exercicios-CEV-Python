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



def resumo(num, aum=0, dim=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço Analisado:\t{moeda(num)}')
    print(f'Dobro do Preço: \t{dobro(num, True)}')
    print(f'Metade do Preço: \t{metade(num, True)}')
    print(f'{aum}% de Aumento: \t{aumentar(num, aum, True)}')
    print(f'{dim}% de Redução: \t{diminuir(num, dim, True)}')
