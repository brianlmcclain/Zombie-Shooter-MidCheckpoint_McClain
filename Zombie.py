import pygame
from pygame.sprite import Sprite
import math
import Player
class zombie(Sprite):

    def __init__(self, ai_game):
        """Initialize the zombie, defines and creates the zombie's resources."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Images/Zombies (2).png')
        self.original_image = pygame.transform.scale(self.image, (100, 100))
        self.original_rect = self.original_image.get_rect()
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.px = ai_game.Player.x
        self.py = ai_game.Player.y

    def player_angle(self, player_coord):
        """Uses trigonometry to make an angle for the player based off of its current position vs its
        former position"""
        player_x, player_y = player_coord[0], player_coord[1]
        rel_x, rel_y = player_x - self.rect.x, player_y - self.rect.y
        if (rel_x ** 2 + rel_y ** 2) > 5:
            angle = (180 / math.pi) * math.atan2(-rel_y, rel_x)
        else:
            angle = self.angle
        return int(angle)

    def rotate_zombie(self, player):
        """Rotates the zombie to face the player using the code defined above"""
        player_coord = [player.rect.x, player.rect.y]
        angle = self.player_angle(player_coord)
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)



    def update(self, ai_game):
        """Adaptive tracking so that the zombie moves towards the player at a constant speed."""

        self.px = ai_game.Player.x
        self.py = ai_game.Player.y

        self.x += self.settings.zombie_speed *  (self.px - self.x) * 0.001
        self.y += self.settings.zombie_speed * (self.py - self.y) * 0.001

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draws the zombie"""
        self.screen.blit(self.image, self.rect)

