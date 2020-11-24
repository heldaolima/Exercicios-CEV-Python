palavras = ('python', 'helder', 'progama', 'kate', 'hounds', 'love', 'shakespeare', 'macbeth', 'amor', 'solidao','medo', 'cloudbusting', 'computador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
