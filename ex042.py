print('--- TRIÂNGULOS 2.0 ---')
a = float(input('Comprimento da reta A: '))
b = float(input('Comprimento da reta B: '))
c = float(input('Comprimento da reta C: '))
if a < b + c and b < a + c and c < a + b:
    print('Forma um triângulo ', end='')
    if a == b == c:
        print('\033[4mequilátero.')
    elif a == b or a == c or b == c:
        print('\033[4misósceles.')
    elif a != b != c:
        print('\033[4mescaleno.')
else:
    print('Não forma triângulo.')
