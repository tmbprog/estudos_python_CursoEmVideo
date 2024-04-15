#criar o módulo "moedas" com as funções aumentar(), diminuir()
#dobro() e metade(). Faça um programa que import e use as funções
from utilidadescv.moedas import moedas
p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos: {moedas.aumentar(p)}')
print(f'Diminuindo em 13%, temos: {moedas.diminuir(p, 13)}')