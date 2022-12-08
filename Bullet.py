import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    def __init__(self, ai_game):
        """Initializes the bullet and creates all of its necesary resources"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.player = ai_game.Player
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.mouse_click_x = ai_game.mouse_click_x
        self.mouse_click_y = ai_game.mouse_click_y

        self.curr_player_x, self.curr_player_y = ai_game.curr_player_x, ai_game.curr_player_y


        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """defines the travel of the bullet and speed"""
        dx = (self.mouse_click_x - self.curr_player_x) * 0.001
        dy = (self.mouse_click_y - self.curr_player_y) * 0.001

        self.x += self.settings.bullet_speed * dx
        self.y += self.settings.bullet_speed * dy

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)