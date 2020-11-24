nums = (int(input('Insira um número: ')),
        int(input('Insira outro número: ')),
        int(input('Insira mais um número: ')),
        int(input('Insira o último número: ')))
print('------------')
print(f'Você inseriu os números {nums}')
print(f'O número 9 foi informado {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O número 3 apareceu primeiro na posição {nums.index(3)+1}')
else:
    print('O valor 3 não foi inserido.')
print('Os valores pares foram: ', end='')
for i in nums:
    if i % 2 == 0:
        print(i, end=' ')
