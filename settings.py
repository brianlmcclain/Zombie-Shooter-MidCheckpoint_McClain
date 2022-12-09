class Settings:
    def __init__(self):
        """Initializes and creates constants and resources used by the rest of the game"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.player_speed = 1.2
        self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 15
        self.zombie_speed = 1
        self.zombie_health = 0