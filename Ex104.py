#Ler e validar um número inteiro
def leiaInt(n):
    n = input(str('Digite um número: '))
    if n.isnumeric():
        return int(n)
    else:
        while n.isnumeric() == False:
            print(f'\033[031mErro! Digite um número inteiro válido!\033[m')
            n = input(str('Digite um número: '))
        return int(n)


num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')