print('--- COMPARADOR DE NÚMEROS ---')
n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o segundo número inteiro: '))
print('--------')
if n1 > n2:
    print('O primeiro número é maior.')
elif n1 < n2:
    print('O segundo número é maior.')
else:
    print('Não há diferença; os números são iguais.')
