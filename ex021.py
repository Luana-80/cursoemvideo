#Desafio21: Fazer um programa que toque musica mp3
import pygame
pygame.init()
pygame.mixer.music.load('house.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
