lista = []
conjunto = []
cont = 0
while True:
    lista.append(input('Nome do aluno: '))
    lista.append(float(input('Sua primeira nota: ')))
    lista.append(float(input('Sua segunda nota: ')))
    conjunto.append(lista[:])
    lista.clear()
    resp = input('Continuar? [S/N]: ').upper()[0]
    while resp not in 'SN':
        resp = input('Continuar? [S/N]: ').upper()[0]
    if resp in 'N':
        break
print('-------- BOLETIM --------')
for i in range(0, len(conjunto)):
    print(f'[{i}]    {conjunto[i][0]}    {((conjunto[i][1] + conjunto[i][2])/2):.1f}')
print('----------------')
while True:
    while True:
        nota = int(input('Faça a sua escolha [999 encerra]: '))
        if 0 <= nota <= len(conjunto) or nota == 999:
            break
    if 0 <= nota <= len(conjunto):
        print(f'Notas de {conjunto[nota][0]}: {conjunto[nota][1]}, {conjunto[nota][2]}')
    elif nota == 999:
        print('----------------')
        print('Fim')
        break

