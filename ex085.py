todos = []
pares = []
impares = []
for i in range(0, 7):
    n = int(input(f'Insira o {i+1}º número: '))
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
todos.append(pares[:])
todos.append(impares[:])
print('-------------------')
print(f'Pares: {todos[0]}')
print(f'Ímpares: {todos[1]}')
