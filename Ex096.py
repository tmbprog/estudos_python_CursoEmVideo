#Cálculo de terreno com função
def area(larg, comp):
    print(f'A área do terreno {larg}x{comp} é de {larg*comp}m²')


larg = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(larg, comp)
