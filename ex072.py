extenso = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Insira um número entre 1 e 20: '))
while n > 20 or n < 0:
    n = int(input('Tente novamente. Insira um número entre 1 e 20: '))
print(f'Você inseriu o número: {extenso[n-1]}')
