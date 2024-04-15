#melhore o 107 para que a edição dos valores monetários fiquem formatados de modo correto
from utilidadescv.moedas import moedas
p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.formatar(p)} é {moedas.formatar(moedas.metade(p))}')
print(f'O dobro de {moedas.formatar(p)} é {moedas.formatar(moedas.dobro(p))}')
print(f'Aumentando 10%, temos: {moedas.formatar(moedas.aumentar(p))}')
print(f'Diminuindo em 13%, temos: {moedas.formatar(moedas.diminuir(p, 13))}')