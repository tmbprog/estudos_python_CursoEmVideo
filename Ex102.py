#Função fatorial() recebe dois parâmetros: 1) "número": que indique o número a calcular,
#2)"show": que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo do cálculo
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número qualquer.
    :param num: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta
    :return: O valor fatorial de um número n.
    """
    if show == True:
        c = num #contador
        f = 1 #fator de multiplicação
        print(f'{num}!:', end='')
        while c > 1:
            f = f*c
            c -= 1
            print(f'{c}', end=' ')
            print('x' if c>=1 else ' = ', end=' ')
        print(f'{f}')
        print('')
    else:
        from math import factorial
        return factorial(num)
    exit()


n = int(input('Digite um número: '))
print(fatorial(n, show=True))
help(fatorial)

