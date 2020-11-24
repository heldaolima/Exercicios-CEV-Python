from datetime import date
print('--- CALCULADOR DE ANO BISEXTO ---')
ano = int(input('Insira o ano, sabendo que \033[4m"0"\033[m retorna o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bisexto.')
else:
    print(f'O ano {ano} não é bisexto.')
