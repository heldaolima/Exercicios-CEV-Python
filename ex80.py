numeros = []
for i in range(0, 5):
    n = int(input('Insira um número: '))
    if i == 0:
        numeros.append(n)
        print('Adicionado na última posição')
    else:
        if n > numeros[-1]:
            numeros.append(n)
            print('Adicionado na última posição')
        elif n < numeros[0]:
            numeros.insert(0, n)
            print('Adicionado na posição 0')
        elif numeros[0] < n < numeros[-1]:
            if numeros[0] < n < numeros[1]:
                numeros.insert(1, n)
                print('Adicionado na posição 1')
            elif numeros[1] < n < numeros[2]:
                numeros.insert(2, n)
                print('Adicionado na posição 2')
            elif numeros[2] < n < numeros[3]:
                numeros.insert(3, n)
                print('Adicionado na posição 3')
print('----------------')
print(f'Lista ordenada: {numeros}')
