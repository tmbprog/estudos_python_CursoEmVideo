#Melhorar o 61 dando a opção para o usuário ver mais termos
a1 = int(input('O primeiro termo da P. A é: '))
r = int(input('A razão da P. A é: '))
termos = a1
cont = 1 #contador = 1, pois a P.A já começa com o a1
print('Os dez primeiros termos da P. A são:')
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termos}', end= '->') #começar com print é importante para imprimir o a1
        termos = termos + r
        cont = cont + 1
    mais = int(input('\nQuantos termos deseja mostrar mais?'))
print('FIM')



