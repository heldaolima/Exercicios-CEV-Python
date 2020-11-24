from time import sleep


def contador (inicio, fim, passo):
    print('-='*40)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(f'{c} ', end='-> ')
            sleep(0.2)
        print('FIM')
    elif inicio > fim:
        passo *= -1
        for c in range(inicio, fim - 1, passo):
            print(f'{c} ', end='-> ')
            sleep(0.2)
        print('FIM')
    elif inicio == fim:
        print(f'Início = Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize agora a contagem: ')
ini = int(input('Insira o início: '))
fim = int(input('Insira o fim: '))
pas = int(input('Insira o passo: '))
contador(ini, fim, pas)
