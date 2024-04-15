def leiaint(msg):
    while True:
        try:
           n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro! Por favor, digite um número válido!\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número válido!\033[m')
            continue
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')
