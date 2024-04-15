#Soma dos números ímpares múltiplos de 3 de 1 a 500
soma = 0
cont = 0 #serve para contar a quantidade de números na cadeia toda
for c in range(0, 501, 3):
        if c%2 != 0:
            cont = cont + 1
            soma = soma + c
            # outras formas de escrever: "cont += 1" e "soma += c"
print(f'A soma de todos os {cont} valores solicitados é: {soma}')






