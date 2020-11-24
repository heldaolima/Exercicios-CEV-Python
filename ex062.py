print('--- PROGRESSÃO ARITMÉTICA 3.0 ---')
primeiro = int(input('Insira o primeiro termo da P.A.: '))
razao = int(input('Insira a razão da P.A.: '))
cont = 1
total = 0
mais = 10
termo = primeiro
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais? '))
print(f'P.A. finalizada com {total} termos mostrados.')
