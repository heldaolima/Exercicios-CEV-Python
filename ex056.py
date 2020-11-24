velhnome = ''
velhomem = 0
totidade = 0
tot20 = 0
for c in range(1, 5):
    print(f'--- {c}º PESSOA ---')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    totidade += idade
    sexo = input('Sexo? [M / F]: ').upper().strip()
    if sexo[0] == 'M':
        if c == 1:
            velhomem = idade
            velhnome = nome
        else:
            if idade > velhomem:
                velhomem = idade
                velhnome = nome
    elif sexo[0] == 'F':
        if idade < 20:
            tot20 += 1
print(f'A média de idade do grupo é {totidade/4:.1f}')
print(f'O homem mais velho tem {velhomem} anos e se chama {velhnome}.')
print(f'No total, {tot20} mulheres têm menos de 20 anos.')
