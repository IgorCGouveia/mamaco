#faça um programa que abra e reproduza um o audio de um arquivo mp3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('py.mp3')
pygame.mixer.music.play()
input('Aperte ENTER para sair')
pygame.mixer.music.stop()