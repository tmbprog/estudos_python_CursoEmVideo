# Recebe: Nome. Ano de Nascimento. CTS. Cadastra no dict: nome, idade, ctps,
#ano de contratação e salário, anos para se aposentar.
from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = datetime.now().year - int(input('Ano de nascimento: ' ))
cadastro['ctps'] = int(input('Carteira de trabalho: '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    aposentadoria = (cadastro['contratação'] + 35) - datetime.now().year
    if aposentadoria <= 0:
        print('Você já contribuiu o suficiente para se aposentar!')
    else:
        cadastro['aposentadoria'] = aposentadoria
print('=='*30)
for k, v in cadastro.items():
    print(f'{k} tem valor {v}')