#Dissecando uma variável. Comando "type" para revelar o valor da variável e "is" para informações sobre ela.
var = input ('Digite algo: ')
cores = {'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'limpo':'\033[m'}
print(var)
print(f'O tipo primitivo desse valor é, \033[31m{type (var)}\033[m')
print(f"{cores['verde']}Está em maiúsculas?, {var.isupper()}{cores['limpo']}")
print(f"{cores['amarelo']}É um número?, {var.isnumeric()}{cores['limpo']}")
print(f"{cores['azul']}É alfabético?, {var.isalpha()}{cores['limpo']}")
print('É alfanumérico?', var.isalnum())
print(f"{cores['roxo']}Está em minúsculas?, {var.islower()}{cores['limpo']}")
print(f"{cores['ciano']}Está capitalizado?, {var.istitle()}{cores['limpo']}")
