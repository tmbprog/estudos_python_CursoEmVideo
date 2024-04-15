#Ler o nome da cidade e dizer se ele começa ou não com "santo"
cidade = input('O nome da sua cidade é: ')
c2 = cidade.split()
Santo = 'Santo'
if c2[0] == Santo:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
#Resolução econômica:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')