import  random

print('--- SORTEAR ALUNOS ---')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
resp = random.choice([n1, n2, n3, n4])
print(f'O aluno sorteado foi {resp}')
