import sys
import pygame
from settings import Settings
from Player import player
from Bullet import bullet
import soundeffects as se
from Zombie import zombie

class ZombieShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, defines and creates the game's resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))#, pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Zombie Shooter")

        self.Player = player(self)
        self.Zombie = zombie(self)
        self.bullets = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.Players = pygame.sprite.Group()
        self.angle = 90
        self.angle_bullet = self.angle
        self.mouse_click_x, self.mouse_click_y = 0, 0
        self.curr_player_x, self.curr_player_y = 0, 0

        self.zombie_health = 3
        self.zombie1_health = self.zombie_health

        self.clock = pygame.time.Clock()
        self.base_font = pygame.font.Font('28 Days Later.ttf', 45)
        self.user_text = '*Space to Survive the Zombie*'
        self.extra_text = '*Shoot it as many times as you can before it catches up*'
        self.input_rect = pygame.Rect(200, 360, 380, 0)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
        self.active = False
        self.s = 0
        self.bullet_zombie_collision = False

        self.score = 0


        se.backgroundsound.play(loops=-1)

    def run_game(self):
        """Charlie Ross helped create start button and start screen"""
        """Makes a home screen so that the game only begins after the spacebar is pressed"""
        """Calls all of the functions defined below to make a playable game"""
        while True:
            if self.s == 0:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.s = 1
                            self.active = True
                        else:
                            pygame.quit()
                            sys.exit()
                self.screen.fill((255, 0, 0))
                if self.active:
                    self.color = self.color_active
                    self.s = 1
                else:
                    self.color = self.color_passive
                pygame.draw.rect(self.screen, self.color, self.input_rect)

                text_surface1 = self.base_font.render(self.user_text, True, (255, 255, 255))
                self.screen.blit(text_surface1, (self.input_rect.x + 20, self.input_rect.y + 5))
                self.input_rect.w = max(100, text_surface1.get_width() + 10)

                text_surface2 = self.base_font.render(self.extra_text, True, (255, 255, 255))
                self.screen.blit(text_surface2, (self.input_rect.x - 150, self.input_rect.y + 60))
                self.input_rect.w = max(100, text_surface2.get_width() + 10)

                pygame.display.flip()
                self.clock.tick(60)
            elif self.s == 1:
                self._check_events()
                self._check_bullet_zombie_collisions()
                self._check_zombie_player_collisions()
                self.Player.update()
                self._update_screen()
                self.Zombie.rotate_zombie(self.Player)
                self.Zombie.update(self)
                self._update_bullets()
                self.Player.rotate_player()



    def _check_events(self):
        """Defines keydown events and mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click_x, self.mouse_click_y = pygame.mouse.get_pos()
                self.curr_player_x, self.curr_player_y = self.Player.rect.x, self.Player.rect.y
                self._fire_bullet()
                se.bulletsound.play()


    def _check_keydown_events(self, event):
        """Defines the arrow keys as player movement, as well as making the q key a quit"""
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


    def _check_keyup_events(self, event):
        """Restricts the code to movement only while a key is pressed down"""
        if event.key == pygame.K_RIGHT:
            self.Player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.Player.moving_left = False
        elif event.key == pygame.K_UP:
            self.Player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.Player.moving_down = False

    def _fire_bullet(self):
        """Used to create a new bullet and call the function from bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Used to call the update from the bullet class as well as define the edge of the screen as boundaries"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if bullet.rect.centerx >= self.settings.screen_width or bullet.rect.centerx < 0:
                self.bullets.remove(bullet)
            if bullet.rect.centery >= self.settings.screen_height or bullet.rect.centery < 0:
                    self.bullets.remove(bullet)


    def _check_bullet_zombie_collisions(self):
        """Code used to detect the collision between a bullet and a zombie"""
        self.zombies.add(self.Zombie)
        collisions = pygame.sprite.groupcollide(self.bullets, self.zombies, True, True)
        if collisions:
            self.bullet_zombie_collision = True
            self.score += 1
            self.settings.zombie_speed += .05

    def _check_zombie_player_collisions(self):
        """Define the Player on Zombie collision and cause you to lose if the zombie touches you."""
        self.zombies.add(self.Zombie)
        collision = pygame.sprite.collide_rect(self.Player, self.Zombie)
        if collision:
            print("Game Over")
            sys.exit()

    def show_score(self):
        """Code used to construst the score/hit board"""
        """I was helped by Eli Watson"""
        score_txt = self.base_font.render("Hits*" + str(self.score), True, (133,133,133))
        self.screen.blit(score_txt, (80,80))


    def _update_screen(self):
        """This is used to update all of the moving objects on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.Player.blitme()
        self.Zombie.blitme()
        self.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()



if __name__ == '__main__':
    """Makes a game instance, and runs the game."""
    ai = ZombieShooter()
    ai.run_game()
