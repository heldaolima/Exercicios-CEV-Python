from datetime import datetime

contmenor = 0
contmaior = 0
atual = datetime.today().year
for c in range(1, 8):
    nasc = int(input(f'Insira o {c}º ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f'\nEntre as idades inseridas, {contmenor} ainda não atingiram a maior idade e {contmaior} já a atingiram.')