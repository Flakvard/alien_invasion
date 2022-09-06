import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage the aliens."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        
        #Load the alien image and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
