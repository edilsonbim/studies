#Desafio é tocar uma musica com python
import pygame
pygame.init()
pygame.mixer.music.load('cinematic.mp3')
pygame.mixer.music.play()
input(print('Aperte enter para finalizar'))
