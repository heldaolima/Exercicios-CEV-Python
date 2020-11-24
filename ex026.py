n = str(input('Insira uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra "A": {n.count("A")}')
print(f'Primeira ocorrência da letra "A": {n.find("A") + 1}')
print(f'Última ocorrência da letra "A": {n.rfind("A") + 1}')
