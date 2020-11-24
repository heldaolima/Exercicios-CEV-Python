from datetime import date

print('--- CATEGORIA DE ATLETA SEGUNDO IDADE ---\n')
nome = input('Insira o nome do atleta: ')
nasc = int(input('Insira o ano de nascimento: '))
print('--------')
ano = date.today().year
idade = ano - nasc
print(f'O atleta {nome} tem {idade} anos. Ele é categorizado como: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade == 10 or idade <= 14:
    print('INFANTIL')
elif idade == 15 or idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')