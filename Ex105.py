#ler várias notas e retornar um dicionárico com total de notas, maior, menor, média e situação (opcional)
def notas(*n,sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não aceitar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    total = len(n)
    maior = max(n)
    menor = min(n)
    soma = 0 #Lembrar que existe a função sum()!!
    for pos, ele in enumerate(n):
        soma += ele
    media = soma/len(n)
    if sit == True:
        if media >= 7.0:
            situacao = str('Boa!')
        if media <= 7.0:
            situacao = str('Ruim!')
        dict = {'Total': total, 'Nota maior': maior, 'Nota menor': menor, 'Média': media, 'Situação': situacao}
        return dict
    else:
        dict = {'Total': total, 'Nota maior': maior, 'Nota menor': menor, 'Média': media}
        return dict


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)