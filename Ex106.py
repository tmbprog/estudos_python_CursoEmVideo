#mini-sistema de utilização do interactive Help
def pyhelp(msg):
    from time import sleep
    print(f'Acessando manual do {msg}')
    sleep(0.5)
    help(msg)
    sleep(0.5)


while True:
    print(f'\033[4;35;43mSistema de Ajuda PyHELP\033[m')
    perg = str(input('Função ou Biblioteca >>'))
    if perg == 'Fim':
        break
    else:
        pyhelp(perg)
