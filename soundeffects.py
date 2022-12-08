import pygame

pygame.mixer.init()

"""Calls audio from the 'soundeffects' file to be used in different functions"""

backgroundsound = pygame.mixer.Sound('soundeffects/trespasser.ogg')
bulletsound = pygame.mixer.Sound('soundeffects/gunshot.wav')
zombiespawn = pygame.mixer.Sound('soundeffects/zombiespawn.wav')
zombiedie = pygame.mixer.Sound('soundeffects/zombiedie.wav')