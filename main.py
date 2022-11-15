lista = []  # LISTA DE PRODUTOS ONDE SERAO ADICIONADOS OS DICIONARIOS
#  INICIO DA FUNÇÃO CADASTRARPRODUTO


def cadastrarproduto(cod):
    print('Você selecionou CADASTRO DE PRODUTO:')
    print('O codigo deste produto sera: {}'.format(cod))
    nome = input('Qual o nome do produto?')
    fabricante = input('Qual o fabricante do produto?')
    valor = float(input('Qual o valor do produto?'))
    dicionario_cadastro = {'nome': nome,
                           'fabricante': fabricante,
                           'valor (R$)': valor,
                           'codigo': cod}
    lista.append(dicionario_cadastro.copy())  # FAZ A COPIA DOS DICIONARIOS PARA A LISTA
#  FIM DA FUNÇÃO CADASTRARPRODUTO

#  INICIO DA FUNÇÃO consultarproduto


def consultarproduto():
    while True:
        try:
            print('Você selecionou CONSULTAR PRODUTO:')
            menu = int(input('Digite a opção desejada:\n'
                             '-1-Consultar Todos os Produtos\n'
                             '-2-Consultar Produto por Codigo\n'
                             '-3-Consultar Produto(s) por Fabricante\n'
                             '-4-Retornar\n'
                             '>>>'))
            if menu == 1:
                print('<<<Bem Vindo a TODOS OS PRODUTOS>>>')
                for dicionario_cadastro in lista:  # SELECIONA CADA DICIONARIO DA LISTA
                    for key, value in dicionario_cadastro.items():  # SELECIONA CADA CONJUNTO DO DICIONARIO
                        print('{} : {}'.format(key, value))
            elif menu == 2:
                print('<<<Bem Vindo a CONSULTAR PRODUTO POR CODIGO>>>')
                cadastro = int(input('Digite o codigo do produto:'))
                for dicionario_cadastro in lista:
                    if dicionario_cadastro['codigo'] == cadastro:  # SE O CODIGO NO DICIONARIO FOR IGUAL AO INPUTADO
                        for key, value in dicionario_cadastro.items():
                            print('{} : {}'.format(key, value))  # IMPRIMIR NA TELA OS DADOS DO PRODUTO
            elif menu == 3:
                print('<<<Bem Vindo a CONSULTAR PRODUTOS POR FABRICANTE>>>')
                fabricante = input('Digite o fabricante:')
                for dicionario_cadastro in lista:
                    if dicionario_cadastro['fabricante'] == fabricante:  # TRANSFORMA O INPUT EM MINUSCULO
                        for key, value in dicionario_cadastro.items():
                            print('{} : {}'.format(key, value))
            elif menu == 4:
                break  # ENCERRA A FUNÇÃO OPÇÃO 'RETORNAR'
            else:
                print('!!!OPÇÃO INVALIDA!!!')
                continue  # VOLTA AO INICIO DA FUNÇÃO CASO DIGITE UM NUMERO NAO CORRESPONDENTE A UMA OPÇÃO
        except ValueError:
            print('!!!CONSULTA INVALIDA!!!')
            continue  # VOLTA AO INICIO DA FUNÇÃO CASO DIGITE UM VALOR NÃO NUMERICO
#  FIM DA FUNÇÃO consultarproduto

#  INICIO DA FUNÇÃO removerproduto


def removerproduto():
    print('Você selecionou REMOVER Produto:')
    cadastro = int(input('Digite o codigo do produto:'))
    for dicionario_cadastro in lista:
        if dicionario_cadastro['codigo'] == cadastro:
            lista.remove(dicionario_cadastro)
            print('Produto excluido')
#  FIM DA FUNÇÃO removerproduto

#  INICIO DA MAIN


print('Bem vindo ao programa de cadastro de produtos do MATHEUS GUSTAVO SCHNEIDER')
codigo = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1-CADASTRAR PRODUTO\n'
                          '2-CONSULTAR PRODUTO(S)\n'
                          '3-REMOVER PRODUTO\n'
                          '4-SAIR\n'
                          '>>>'))
        if opcao == 1:
            codigo += 1
            cadastrarproduto(codigo)
        elif opcao == 2:
            consultarproduto()
        elif opcao == 3:
            removerproduto()
        elif opcao == 4:
            print('Programa Encerrado!')
            break
        else:
            print('!!!OPÇÃO INVALIDA!!!')
            continue
    except ValueError:
        print('!!!OPÇÃO INVALIDA!!!')
        continue
#  FIM DA MAIN
