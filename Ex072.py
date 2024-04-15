#Ler um número entre 0 e 20 e mostrar ele por extenso
n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n not in range(0,21):
    n = int(input('Tente novamente. Digite um número 0 e 20: '))
print(f'O número digitado foi: {n_extenso[n]}')
