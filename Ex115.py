#Mini-sistema MODULARIZADO que cadastre pessoas pelo nome e idade em um arquivo texto simples.
#O sistema tem duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
import Ex115mod

while True:
    op = Ex115mod.menu()
    if op == 1:
        Ex115mod.leitura()
    if op == 2:
        while True:
            print('==' * 30)
            print(f'\033[1m{"Cadastro de Pessoa".upper():^60}\033[m')
            print('==' * 30)
            nome = str(input('Nome: '))
            idade = Ex115mod.leiaInt('Idade: ')
            Ex115mod.cadastro(nome, idade)
            continuar = str(input('Continuar cadastrando[S/N]?'))[0].upper().strip()
            if continuar in 'Nn':
                break
    if op == 0:
        Ex115mod.novo()
        continue
    if op == 3:
        break
print('Volte Sempre')

#Ver a resolução conforme o Guanabara em ex115G