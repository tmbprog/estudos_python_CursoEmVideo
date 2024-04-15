#Ler 3 números e dizer qual é o maior e qual o menor
n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))
n3 = int(input('Número 3:'))
if (n1>n2 and n1>n3):
    print(f'O número maior é {n1}')
if (n2>n1 and n2>n3):
    print(f'O maior número é {n2}')
if (n3>n1 and n3>n2):
    print(f'O maior número é {n3}')
if (n1<n2 and n1<n3):
    print(f'O menor número é {n1}')
if (n2<n1 and n2<n3):
    print (f'O menor número é {n2}')
if (n3<n1 and n3<n2):
    print(f'O menor número é {n3}')
# modo simpliticado
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f'menor: {menor}')
# só fazer o mesmo para >
