frase = input('Insira uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = [::-1] -> Faria o mesmo que o FOR, mas no puro fatiamento
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('Mão temos um palíndromo')
