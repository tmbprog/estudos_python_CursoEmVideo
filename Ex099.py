#Função maior
def maior(* n):
    print('Os valores informados foram:', end= ' ')
    for c in n:
        print(c, end= ' ')
    print(f'\nA quantidade de números informados foi: {len(n)}')
    print(f'E o maior valor entre eles é {max(n)}')
    print('=='*30)


maior(2, 4, 8, 7, 6, 5)
maior(3, 4, 8, 9)
maior(2, 1, 3)
maior(0)
#maior() #fazendo com o for, como no vídeo, evita o erro do ()