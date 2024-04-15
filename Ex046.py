#Contagem regressiva do ano novo. Intervalo 1s
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[31mFELIZ ANO NOVO!!!\033[0m')