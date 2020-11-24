print('--- CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO ---')
a = float(input('Comprimento da reta A: '))
b = float(input('Comprimento da reta B: '))
c = float(input('Comprimento da reta C: '))
if a < b + c and b < a + c and c < a + b:
    print('Forma triângulo.')
else:
    print('Não forma triângulo.')
