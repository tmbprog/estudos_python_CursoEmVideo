#Financiamento de casa. Dados: valor da casa, salário e anos.
#Calcular o valor da prestação sabendo que ela não pode exceder 30% do salário,  senão é negado o empréstimo.
vc = float(input('Valor da casa: R$'))
sl = float(input('Salário: R$'))*30/100
ano = int(input('Anos de financiamento: '))*12
p = vc/ano
if p < sl:
    print(f'A prestação do seu financiamento será de \033[34mR${p:.2f}\033[m por mês')
else:
    print (f'Seu empréstimo foi negado, pois a prestação, de \033[31mR${p:.2f}\033[m, excede 30% do seu salário.')