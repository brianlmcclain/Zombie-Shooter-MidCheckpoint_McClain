import pygame
import math
class player:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/Player.bmp')
        self.original_image = pygame.transform.scale(self.image, (150,150))
        self.original_rect = self.original_image.get_rect()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.angle = -90
        self.prev_coordinate = pygame.mouse.get_pos()
        self.health = 100

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        self.rect.x = self.x
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        self.rect.y = self.y

    def mouse_angle(self, coordinate):
        mouse_x, mouse_y = coordinate[0], coordinate[1]
        rel_x, rel_y = mouse_x - self.prev_coordinate[0], mouse_y - self.prev_coordinate[1]
        self.prev_coordinate = coordinate
        if (rel_x ** 2 + rel_y ** 2) > 5:
            angle = (180 / math.pi) * math.atan2(-rel_y, rel_x)
        else:
            angle = self.angle
        return int(angle)
    def rotate_player(self):
        coordinate =  pygame.mouse.get_pos()
        self.angle = self.mouse_angle(coordinate)
        self.image = pygame.transform.rotate(self.original_image, self.angle + 90)
        self.rect = self.image.get_rect(center=self.rect.center)
    def move(self, coordinate):
        self.rect.center = coordinate

    def blitme(self):
        self.screen.blit(self.image, self.rect)
