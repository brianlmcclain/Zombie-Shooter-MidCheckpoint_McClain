import sys
import pygame
from settings import Settings
from Player import player
from Bullet import bullet
import soundeffects as se
class ZombieShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))#, pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Zombie Shooter")

        self.Player = player(self)
        self.bullets = pygame.sprite.Group()
        self.zombie = pygame.sprite.Group()
        self.angle = 90
        self.angle_bullet = self.angle
        self.mouse_click_x = 0
        self.mouse_click_y = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.Player.update()
            self._update_screen()
            self._update_bullets()
            self.Player.rotate_player()
            se.backgroundsound.play(loops=-1)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.Player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.Player.moving_left = True
        elif event.key == pygame.K_UP:
              self.Player.moving_up = True
        elif event.key == pygame.K_DOWN:
              self.Player.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.MOUSEBUTTONDOWN:
            self._fire_bullet()
            se.bulletsound.play()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.Player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.Player.moving_left = False
        elif event.key == pygame.K_UP:
            self.Player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.Player.moving_down = False
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            mouse_x, mouse_y = pygame.gouse.get_pos()
            if bullet.rect.centerx == mouse_x or bullet.rect.centery == mouse_y:
                self.bullets.remove(bullet)
            if bullet.rect.centerx >= self.settings.screen_width or bullet.rect.centerx < 0:
                self.bullets.remove(bullet)
            if bullet.rect.centery >= self.settings.screen_height or bullet.rect.centery < 0:
                    self.bullets.remove(bullet)



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.Player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = ZombieShooter()
    ai.run_game()
