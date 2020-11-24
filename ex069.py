contidade = 0
contm = 0
contfid = 0
print('-'*30)
print(f'{"CADASTRO DE PESSOAS":^30}')
print('-'*30)
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo in 'M':
        contm += 1
    elif sexo in 'F':
        if idade < 20:
            contfid += 1
    print('-'*40)
    escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar [S/N]? ').strip().upper()[0]
    if escolha in 'N':
        break
    print('-'*40)
print('-'*40)
print('Cadastros recolhidos...')
print(f'\nTotal de pessoas com mais de 18 anos: {contidade}')
print(f'Total de homens cadastrados: {contm}')
print(f'Total de mulheres com menos de 20 anos: {contfid}')
