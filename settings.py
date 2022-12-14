class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initilize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        #Alien settings
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 0.03 #0.03 Gives only the same alien_points = 50

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 4.5
        self.bullet_speed = 7.5
        self.alien_speed = 7.0

        #Fleet_directions of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increased_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
        