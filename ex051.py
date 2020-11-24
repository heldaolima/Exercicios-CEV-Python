print('--- PROGRESSÃO ARITMÉTICA ---')
primeiro = int(input('Insira o primeiro termo da P.A.: '))
razao = int(input('Insira a razão da P.A.: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+1,razao):
    print(c)
