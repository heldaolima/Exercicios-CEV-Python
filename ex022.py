nome = str(input('Insira o seu nome completo: '))
ns = nome.split()
ns2 = ''.join(ns)
print(f'Em maiúsculas: {nome.upper()}\n'
      f'Em minúsculas: {nome.lower()}\n'
      f'O nome completo tem {len(ns2)} letras (sem espaços)\n'
      f'O 1º nome tem {len(ns[0])} letras.')
