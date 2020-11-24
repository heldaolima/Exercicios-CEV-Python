print(f'{" TABUADA ":-^20}')
while True:
    n = int(input('Qual tabuada deseja ver? '))
    print('-----------------')
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-----------------')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')