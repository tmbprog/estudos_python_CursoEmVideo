# Algoritmo que lê um número e mostra o seu dobro, o triplo e a raiz quadrada
n = int(input('Digite um número:'))
print(f'O dobro do número digitado é: \033[34m{n*2}\033[m; \nO triplo é: \033[35m{n*3};\033[m\nA raíz quadrada é: \033[36m{n**(1/2):.2f}')