def metade(n, sit=False):
    n = n/2
    if sit == True:
        return formatar(n)
    return n


def dobro(n,sit=False):
    n = n*2
    if sit == True:
        return formatar(n)
    else:
        return n


def aumentar(a, b=0.0, sit=False):
    """
    -> aumenta preço
    :param a: valor
    :param b: (opcional) permite escolher a porcentagem
    :return: retorna por padrão 10% ou a porcentagem escolhida
    """
    if sit == True:
        if b!= 0:
            a = a + a * (b / 100)
            return formatar(a)
        if b == 0:
            a = a + a * (10 / 100)
            return formatar(a)
    else:
        if b != 0:
            return a + a * (b / 100)
        else:
            return a + a * (10 / 100)



def diminuir(a, b=0.0, sit = False):
    """
    -> diminuir preço
    :param a: valor
    :param b: (opcional) permite escolher a porcentagem
    :return: retorna por padrão - 10% ou a porcentagem escolhida
    """
    if sit == True:
        if b != 0:
            a = a - a * (b / 100)
            return formatar(a)
        if b == 0:
            a = a - a * (10 / 100)
            return formatar(a)
    else:
        if b != 0:
            return a - a * (b / 100)
        else:
            return a - a * (10 / 100)


def formatar(n):
    return f'R${n:.2f}'.replace('.',',')


def resumo(a=0, b=0, c=0):
    print('--'*20)
    print(f'{"Resumo do Valor Analisado":^40}')
    print('--'*20)
    print(f'Valor analisado:     \t{formatar(a)}')
    print(f'O dobro do preço:    \t{dobro(a, True)}')
    print(f'Metade do preço:     \t{metade(a, True)}')
    print(f'{b}% de aumento:     \t{aumentar(a, b, True)}')
    print(f'{c}% de redução:     \t{diminuir(a, c, True)}')
    print('--'*20)
    exit()