print('--- PROGRESSÃO ARITMÉTICA 2.0 ---')
primeiro = int(input('Insira o primeiro termo da P.A.: '))
razao = int(input('Insira a razão da P.A.: '))
cont = 0
termo = primeiro
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    cont += 1
print('FIM')
