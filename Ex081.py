#Ler vários números e mostrar: a) quantos números foram digitados, b) lista ordenada, c) se o 5 foi digitado
lista = []
while True:
    n = int(input('Digite um valor: ')) #Esse input poderia vir logo dentro do () do append
    lista.append(n)
    op = input('Continuar[S/N]?')
    if op == 'N':
        break
print('=='*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os números organizados em ordem decrescente são: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está lista')