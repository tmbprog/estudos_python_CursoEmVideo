#Partindo da data de nascimento saber se o atleta é Mirim = 9anos, 14 inf, 19, jr, 20 senior, acima master
from datetime import datetime
data = int(datetime.now().year)
ano = int(input('Insira o ano de nascimento do atleta: '))
idade = int(data - ano)
if idade <= 9:
    print('Deve ser inscrito na categoria \033[1mMirim')
elif idade > 9 and idade <= 14:
# É possível escrever só idade <= 14
    print('Deve ser inscrito na categoria \033[1mInfantil')
elif idade > 14 and idade <= 19:
    print('Deve ser inscrito na categoria \033[1mJúnior')
elif idade <= 25:
    print('Dever ser inscrito na categoria \033[1mSénior')
else:
    print('Deve ser inscrito na categoria \033[1mMaster')
