#Ler um número de 0 a 9999 e mostrar os dígitos (unidade, dezena, centena e milhar)
n1 = int(input('Digite um número de 0 a 9999: '))
# Com str dá erro para números menores que 4 dígitos, então é preciso resolver com a matemática
u = n1//1%10
d = n1//10%10
c = n1//100%10
m = n1//1000%10
print(f'Unidade: {u}')
print (f'Dezena: {d}')
print (f'Centena: {c}')
print (f'Milhar: {m}')