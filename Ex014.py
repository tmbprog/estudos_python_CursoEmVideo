#Conversor de Temperaturas
tc = float(input('Digite a temperatura em graus célsius:'))
tf = ((9*tc)/5)+32
# A fórmula poderia ser escrita sem parênteses, pois segue a ordem de precedência dos operadores.
print (f'Essa temperatura corresponde em Fahrenheit é: \033[37m{tf}')
