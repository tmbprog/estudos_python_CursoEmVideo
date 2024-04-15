#Colocar formatação como parâmetro
from utilidadescv.moedas import moedas
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.formatar(p)} é {moedas.metade(p, sit=True)}')
print(f'O dobro de {moedas.formatar(p)} é {moedas.dobro(p, sit=True)}')
print(f'Aumentando 10%, temos: {moedas.aumentar(p, sit=True)}')
print(f'Diminuindo em 13%, temos: {moedas.diminuir(p, 13, sit=True)}')