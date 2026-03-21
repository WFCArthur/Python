# Faça um programa em Python que abra e reproduza o áudio de arquivo MP3.
import pygame 
pygame.init()
pygame.mixer.music.load('tes.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
pygame.event.wait()