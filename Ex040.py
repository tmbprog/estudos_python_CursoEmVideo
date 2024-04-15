#Média do aluno com comentários
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2)/2
print(f'Sua média é: {média} ')
if média < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif média > 5.0 and média <= 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m')
else:
    print('\033[32mAPROVADO!!\033[m')