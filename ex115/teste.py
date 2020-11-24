from exerc.ex115.lib.interface import *
from exerc.ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    x = leiaInt('Sua opção: ', 3, 2)
    if x == 1: #listar o conteúdo do arquivo (Lê-lo)
        lerArquivo(arq)
    elif x == 2: #cadastrar nova pessoa
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif x == 3:
        titulo('Saindo do sistema... ')
        break