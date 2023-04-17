from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do sistema
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        # Digitou uma opção errada
        print('\033[31mERRO! Digite uma opção válida\33[m')
    sleep(2)