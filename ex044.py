prod = float(input('Insira o valor da sua compra: R$'))
print('''Escolha a sua forma de pagamento (outro número cancela a compra):
[ 1 ] À vista dinheiro/cheque: \033[4m10% de desconto\033[m
[ 2 ] À vista no cartão: \033[4m5% de desconto\033[m
[ 3 ] Em até 2x no cartão: \033[4mPreço normal\033[m
[ 4 ] 3x ou mais no cartão: \033[4m20% de juros\033[m''')
escolha = int(input('Sua escolha: '))
print(f'Você escolheu a opção {escolha}')
print('---------')

if escolha == 1:
    novo = prod - (prod * 10/100)
    print(f'A sua compra terá 10% de desconto. Assim, você pagará \033[4mR${novo:.2f}')
elif escolha == 2:
    novo = prod - (prod * 5/100)
    parcelas = novo / 2
    print(f'A sua compra terá 5% de desconto.')
    print(f'Assim, o novo preço será de \033[4mR${novo}\033[m, que você pagará em 2x de \033[4mR${parcelas:.2f}')
elif escolha == 3:
    print(f'A sua compra permanecerá com o valor de R${prod:.2f}')
elif escolha == 4:
    divid = int(input('Em quantas parcelas deseja dividir? '))
    novo = (prod * 20/100) + prod
    parcelas = novo / divid
    print(f'A sua compra terá 20% de juros.')
    print(f'Assim, o novo preço será de \033[4mR${novo}\033[m, que você pagará em {divid}x de \033[4mR${parcelas}')
else:
    print('Compra cancelada.')