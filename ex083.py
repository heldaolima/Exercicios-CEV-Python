expressao = input('Insira uma expressão: ')
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('------------------------------------')
if len(pilha) == 0:
    print('Expressão corretamente construída!')
else:
    print('Expressão construída de forma errada!')
