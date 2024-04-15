#Resumo de todas as funções do módulo moedas()
from utilidadescv import moedas

n = float(input('Digite um valor: R$ '))
print(moedas.resumo(n, 80, 35))