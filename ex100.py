from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(0, 5):
        val = randint(0, 10)
        lista.append(val)
        print(val, end=' ')
        sleep(0.3)
    print('FIM')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando todos os valores pares da lista {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
