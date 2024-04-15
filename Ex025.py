# Programa que identifica Silva no nome
nome = input('Nome completo:')
if 'silva' in nome.lower():
 #importante sempre converter para .upper ou lower para evitar qualquer conflito com a digitação
    print('Seu nome tem Silva')
else:
    print('Você não tem Silva no nome')
#Resolução do professor
nom = str(input('Qual o seu nome completo? ')).strip()
print(f"Seu nome tem Silva? {'silva' in nom.lower()}")