# Ler dois valores e mostrar menu: [1]somar, [2]multiplicar, [3]maior valor [4]novos números [5]sair
n = 1
while n != 5:
    print('Com quais valores você quer trabalhar?') #Guanabara fez com v1 e v2 fora do while
    v1 = float(input('Primeiro valor: '))
    v2 = float(input('Segundo valor: '))
#a opção 4 fica um pouco sem sentido quando v1 e v2 estão dentro do while
    print('''O que você deseja fazer?
    [01] Somar
    [02] Multiplicar
    [03] Ver maior valor
    [04] Novos números      
    [05] Sair''')
    op = int(input('Digite sua opção:'))
    if op == 5:
        n = 5
    elif op == 1:
        print(f'\033[32m{v1} + {v2} = {v1+v2}\033[m')
        sair = str(input('Deseja continuar trabalhando? [S/N]')).upper().strip()
        if sair == 'N':
            n = 5
    elif op == 2:
        print(f'\033[32m{v1} x {v2} = {v1*v2}\033[m')
        sair = str(input('Deseja continuar trabalhando? [S/N]')).upper().strip()
        if sair == 'N':
            n = 5
    elif op == 3:
        list = [v1,v2]
        print(f'\033[32mO maior valor é: {max(list)}\033[m')
        sair = str(input('Deseja continuar trabalhando? [S/N]')).upper().strip()
        if sair == 'N':
            n = 5
print('Volte sempre!')