#Programa que diz se a frase digitada é um palíndromo (ex: a sacada da casa)
frase = str(input('Escreva a frase: ')).lower()
junto = ''.join(frase.split()) #comando para remover todos os espaços da frase
print(junto)
pali = (junto[::-1]) #comando para inverter a string
print(pali)
if junto == pali:
    print('É um palíndromo!')
else:
    print('Não é palíndromo!')
print('OUTRA SOLUÇÃO!!!')
#Usando o for para ler invertido:
inverso = ''
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]
print(inverso)