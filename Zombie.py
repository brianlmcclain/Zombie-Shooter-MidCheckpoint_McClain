import pygame
from pygame.sprite import Sprite
from random import randint

class Zombie(Sprite):

    def __init__(self, ai_game):

        super().__init()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.angle = ai_game.angle

        self.image = pygame.image.load('Images/Zombies.bmp')
        self.rect = self.image.get_rect()

        randnum = randint(1,4)
        if randnum == 1:
            self.rect.x = 0
            self.rect.y = self.ai_game.settings.screen_height
        elif randnum == 2

        self.rect.x = self.rect.centerx
        self.rect.y = self.rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.angle == 0:
            self.y -= self.settings.zombie_speed

