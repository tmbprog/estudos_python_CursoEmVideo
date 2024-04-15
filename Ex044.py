"""Valor do produto de acordo com o pagamento: à vista dinheito ou cheque: 10% de desconto; à vista cartão: 5% desconto;
em até 2xcartão: preço normal; 3xno cartão: 20%juros"""
print(f"{' Lojas Melo ':=^43}")
vl = float(input('Valor do produto: R$'))
print('Escolha sua forma de pagamento:')
print('Digite: \n 01 para pagamentos à vista (dinheiro ou cheque);\n 02 para pagamentos à vista no cartão;')
print(' 03 para parcelamentos em 2 vezes;\n 04 para parcelamentos acima de 3 vezes;')
pg = input('Forma de pagamento: ')
if pg == '01':
    print(f'Seu produto, com desconto de 10%, ficará por: R${vl - (vl*10/100):.2f}')
elif pg == '02':
    print(f'Seu produto, com desconto de 5%, ficará por: R${vl - (vl*5/100):.2f}')
elif pg == '03':
    print(f'Não há juros para parcelamentos em 2x, você pagara: R${vl:.f}')
elif pg == '04':
    parc = int(input('Quantas parcelas? '))
    print(f'''Seu produto, parcelado em {parc} vezes, terá um acréscimo de 20% e ficará por: R${vl + (vl*20/100):.2f}.
Sendo que cada parcela custará: R${(vl + vl*20/100)/parc:.2f}''')
else:
    print('\033[31mOpção inválida. Tente novamente.')