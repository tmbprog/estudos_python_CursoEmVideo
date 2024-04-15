#Programa que verifica se o site pudim está acessível
import urllib.request
try:
    pudim = "http://www.pudim.com.br/"
    pagina = urllib.request.urlopen(pudim)
    print('A página Pudim está funcionando')
except:
    print('Não foi possível acessar a página pudim')
