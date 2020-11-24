print('--- ÍNDICE DE MASSA CORPORAL ---')
peso = float(input('Insira o seu peso em Kg: '))
alt = float(input('Insira a sua altura em metros: '))
imc = peso/alt**2
print('----------')
print(f'O seu IMC resulta em {imc:.1f}. Você está ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc == 18.5 or imc < 25:
    print('no PESO IDEAL')
elif imc == 25 or imc < 30:
    print('em SOBREPESO')
elif imc == 30 or imc < 40:
    print('em OBESIDADE')
else:
    print('em OBESIDADE MÓRBIDA')
