# Ler nome, idade e sexo de 4 pessoas. Mostar: media de idade, o nome do H mais velho e quantas M tem menos de 20anos
sid = 0
list = []
cont = 0
for p in range(1,5):
    nom = str(input(f'Nome {p}: '))
    id = int(input(f'Idade {p}: '))
    sex = str(input(f'Sexo {p} [M]masculino ou [F]feminino: '))
    print("="*10)
    sid = sid + id
    if sex == 'F' and id < 20:
        cont = cont + 1
    if sex == 'M':
        list = list + [id]
        if sex == 'M' and max(list) == id:
            nome = nom
print(f'Média de idade: {sid/4}')
print(f'Mulheres com menos 20 anos: {cont}')
print(f'O homem mais velho é {nome}, com {max(list)} anos.')
