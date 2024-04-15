#Dizer se um jovem precisa se alistar, se já passou da hora ou se ainda vai
from datetime import datetime
data = int(datetime.now().year)
#Outra opção: import date e faça: "date.today().year
ano = int(input('Informe o ano do seu nascimento:'))
if data - ano < 18:
    print('Você ainda não precisa se alistar!')
    print(f'Faltam \033[1m{18-(data-ano)} anos\033[m para você se alistar.')
elif data - ano == 18:
    print('\033[31mVocê precisa se alistar esse ano!')
else:
    print('A data do seu alistamento já passou...')
    print(f'Seu alistamento deveria ter sido há \033[1m{(data-ano)-18} anos.')
