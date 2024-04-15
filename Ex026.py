# Verificar em uma frase: quantos vezes aparece a letra "a", quando aparece a primeira e a última vez.
frase = str(input('Digite uma frase: ')).strip()
#Importante o .strip() para eliminar os espaços
frase2 = frase.lower()
print(f"O número de vezes que a letra A aparece na sua frase é: {frase2.count('a')}")
print(f"A primeira vez ela aparece é na posição {frase2.find('a')+1}.")
#colocar o +1 para indicar a posição que o usuário vê
print(f"A última vez que ela aparece é na posição {frase2.rfind('a')+1}.")