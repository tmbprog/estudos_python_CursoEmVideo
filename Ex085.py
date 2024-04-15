#Digitar 7 valores. Cadastrar numa única lista que mantenha separado pares e ímpares.
#Final mostrar pares e ímopares de forma crescente.
list_par_impar = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if n%2 == 0:
        list_par_impar[0].append(n)
    else:
        list_par_impar[1].append(n)
list_par_impar[0].sort()
list_par_impar[1].sort()
print(f'Os números pares em ordem crescente são {list_par_impar[0]}')
print(f'e os número ímpares são {list_par_impar[1]}')
