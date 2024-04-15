#Função voto() que recebe ano de nascimento e retorna: vt negado, opcional ou obrigatório
def voto(n):
    from datetime import date
    idade = date.today().year - n
    if idade >= 18 and idade < 65:
        return f"Com {idade} anos o voto é obrigatório!"
    if idade >= 16 and idade < 18 or idade >= 65:
        return f"Com {idade} anos o voto é opcional!"
    else:
        return f"Com {idade} anos você ainda não pode votar!"


nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))