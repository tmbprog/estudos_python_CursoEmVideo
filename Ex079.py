#Receber vários valores numéricos. Adicionar na lista (exceto se já estiver). Mostrar todos os valores em ordem crescente.
lista = []
while True:
    n = int(input('Digite um valor para cadastrar: '))
    if n not in lista:
        lista.append(n)
        op = input('Deseja continuar [S/N]?').strip().upper()[0]
        if op == 'N':
            break
    else:
        print('Número já castrado. Tente outro!')
lista.sort()
print(f'Os números cadastrados foram {lista}')

