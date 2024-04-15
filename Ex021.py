#Abrir e reproduzir um arquivo mp3
import pygame
# pygame: biblioteca usada para criar jogos, mas que possui muitas outras funções
pygame.mixer.init()
pygame.mixer.music.load('beatles01.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass