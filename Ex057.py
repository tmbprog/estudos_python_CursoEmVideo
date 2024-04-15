#Lê o sexo da pessoa, mas só aceite valores M ou F
sexo = str(input('Qual o seu sexo[M/F]?')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! \nQual o seu sexo[M/F]?')).upper().strip()[0]
print(f'Sexo {sexo} cadastrado com sucesso')

