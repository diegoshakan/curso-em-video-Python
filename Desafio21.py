import pygame

'''Faça um programa que seja capaz de tocar um mp3'''

pygame.init()
pygame.mixer.music.load('oi.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''É necessário instalar o pacote do pygame, não é o foco do curso neste momento
como dito pelo prof Gustavo Guanabara no desafio.'''