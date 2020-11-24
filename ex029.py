carro = float(input('Qual a velocidade regitrada em km/h do carro? '))
if carro > 80:
    ult = carro - 80
    multa = 7 * ult
    print(f'\033[31mO carro estava {ult:.2f}km/h acima do limite.\n\033[4mAssim, será multado em \033[1mR${multa:.2f}\033[m')
else:
    print('\033[4;34mVelocidade dentro dos limites.\033[m')
print('--------')
print('\033[32mDirija com cuidado.')
