def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: (opcional) Mostrar ou não os cálculos
    :return: resultado do fatorial de num
    """
    fat = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= i
    return fat


print('=================')
print(fatorial(10, show=True))
