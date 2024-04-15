#Calcular o IMC e dizer se: abaixo(<18.5), ideal (entre 18.5 e 25), sobrepeso (25-30), obesidade(30-40) e ob.mórbida(acima de 40)
a = float(input('Altura em metros: '))
p = float(input('Peso em Kg: '))
imc = p/(a*a)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc < 25:
# outra opção de escrita: "18.5 <= imc < 25"
    print('Você está no seu peso ideal!')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')
print(f'Seu IMC é: {imc:.2f}')