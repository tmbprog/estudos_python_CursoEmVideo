#Menu
def menu():
    print('=='*30)
    print(f'\033[1m{"Menu Principal".upper():^60}\033[m')
    print('=='*30)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar uma nova pessoas\n3 - Sair\n0 - Novo')
    print('=='*30)
    try:
        menu = int(input('Sua opção: '))
    except:
        print(f'\033[31mOpção inválida! Tente novamente!\033[m')
    else:
        return menu


#cadastrar
def cadastro(nome='desconhecido', idade=0):
    texto = (f'{nome:<30}{idade:>25} anos')
    arquivo = open('NomeIdade.txt', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


#novo
def novo():
    print('=='*30)
    print('\033[31mAtenção! Esse processo apagará todos os dados cadastrados!\033[m')
    op = str(input('Deseja continuar[S/N]?'))
    if op == 'S':
        arquivo = open('NomeIdade.txt', 'w')
        print('Formatação realizada com sucesso!')
        arquivo.close()
    else:
        print('Ok! Saindo do modo formatação...')

#validar inteiro
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número válido!\033[m')
            continue
        else:
            return n

#ler
def leitura():
    print('==' * 30)
    print(f'\033[1m{"Pessoas Cadastradas".upper():^60}\033[m')
    print('==' * 30)
    arquivo = open('NomeIdade.txt', 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()


