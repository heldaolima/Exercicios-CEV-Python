sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Opção inválida. \nInsira o seu sexo [M/F]: ').strip().upper()[0]
print(f'O seu sexo é {sexo}')
