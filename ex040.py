print('--- SITUAÇÃO DO ALUNO ---')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('-------')
media = (n1 + n2) / 2
print(f'A média foi de {media:.1f}')
if media < 5:
    print('\033[4mREPROVADO')
elif media == 5 or media <= 6.9:
    print('\033[4mRECUPERAÇÃO')
elif 7 <= media:
    print('\033[4mAPROVADO')
